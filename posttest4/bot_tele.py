import os
# import types
from telebot import types
import telebot
import ast
from telebot.util import quick_markup

BOT_TOKEN = "6891204613:AAFQFq9qtS7S4V0MCdHjlZCZLWmYtswYbWo"

stringList = {"LED1": "ON", "LED2": "OFF", "LED3": "ON"}


authorize ={"a1560123529":"LED1", "a1467110098":"LED2"}


# crossIcon = u"\u274C"

def makeKeyboard():
    markup = types.InlineKeyboardMarkup()

    for key, value in stringList.items():
        if value == "ON":
            value = u"\u2705"
        else:
            value = u"\u274C"
        markup.add(types.InlineKeyboardButton(text=key+" "+value,
                                              callback_data="['key', '" + key + "', '" + value + "']"))
    return markup


bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello', 'status', 'id'])
def send_welcome(message):
    if message.text[1:] == 'status':
        # text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
        # sent_msg = bot.send_message(message.chat.id, text)
        
        bot.reply_to(message, "Berikut Status LED.", reply_markup=makeKeyboard(),parse_mode="HTML")
        # bot.register_next_step_handler(sent_msg, echo_all)
        # bot.reply_to(message, "berikut adalah status dari iot"+ str(message.id)+ str(message),)
        return
    elif message.text[1:] == 'id' :
        bot.reply_to(message, "Berikut adalah id tele anda : "+str(message.from_user.id))
    # bot.reply_to(message, message.text[1:]+" Howdy, how are you doing?")



@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):

    if (call.data.startswith("['key'")):
        print(f"call.data : {call.data} , type : {type(call.data)}")
        print(f"ast.literal_eval(call.data) : {ast.literal_eval(call.data)} , type : {type(ast.literal_eval(call.data))}")
        valueFromCallBack = ast.literal_eval(call.data)[1]
        keyFromCallBack = ast.literal_eval(call.data)[2]
        print("berikut adalah id call : "+str(call.from_user.id))
        # for i in range(len(authorize)):
        # print(keyFromCallBack)
        if valueFromCallBack == "LED3" :
            bot.answer_callback_query(callback_query_id=call.id,
                            show_alert=True,
                            text="You Clicked " + valueFromCallBack + " and LED is " + keyFromCallBack)
            
        elif valueFromCallBack == authorize["a"+str(call.from_user.id)] :
            bot.answer_callback_query(callback_query_id=call.id,
                            show_alert=True,
                            text="You Clicked " + valueFromCallBack + " and LED is " + keyFromCallBack)
        
        else:
            bot.answer_callback_query(callback_query_id=call.id,
                            show_alert=True,
                            text="anda tidak punya authorize")



        # bot.answer_callback_query(callback_query_id=call.id,
        #                       show_alert=True,
        #                       text="You Clicked " + valueFromCallBack + " and LED is " + keyFromCallBack)

    if (call.data.startswith("['value'")):
        keyFromCallBack = ast.literal_eval(call.data)[1]
        del stringList[keyFromCallBack]
        bot.edit_message_text(chat_id=call.message.chat.id,
                              text="Here are the values of stringList",
                              message_id=call.message.message_id,
                              reply_markup=makeKeyboard(),
                              parse_mode='HTML')
        

# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

bot.infinity_polling()