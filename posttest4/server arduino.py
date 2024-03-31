from flask import Flask, request, jsonify
import json
app = Flask(__name__)



# datas = 0

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    print("pesan dari :", uuid)
    content = request.json
    print(content)
    f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/data.txt", "r")
    # f.write(f"{data}")
    # f.read()
    bagus = f.read()
    return f"{bagus}"

@app.route('/')
def des():
    return """
    <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
    <body style="background-color:#27a7b8">
    <div style="position: absolute; top: 40vh;left: 45vw;">
    <br>
    <center style="font-size:40px;">frekuensi : </center>
    <center id="nyaring" style="font-size:40px;">nyaring</center>
    <br>
    <center style="font-size:40px;">brightness : </center>
    <center id="terang" style="font-size:40px;">terang</center>
    </div>
    <script>
    setInterval(function() {
    fetch('http:\/\/127.0.0.1:5000/nyaring', {
    method: 'POST'
})
   .then(response => response.json())
   .then(json => document.getElementById("nyaring").innerHTML = json["data"]);
    }, 60 * 1); // 60 * 10 milsec
    </script>
    <script>
    setInterval(function() {
    fetch('http:\/\/127.0.0.1:5000/terang', {
    method: 'POST'
})
   .then(response => response.json())
   .then(json => document.getElementById("terang").innerHTML = json["data"]);
    }, 60 * 1); // 60 * 10 milsec
    </script>
    </body>
    </html>
    """



    
# <style>
# .switch {
#   position: relative;
#   display: inline-block;
#   width: 60px;
#   height: 34px;
# }

# .switch input { 
#   opacity: 0;
#   width: 0;
#   height: 0;
# }

# .slider {
#   position: absolute;
#   cursor: pointer;
#   top: 0;
#   left: 0;
#   right: 0;
#   bottom: 0;
#   background-color: #ccc;
#   -webkit-transition: .4s;
#   transition: .4s;
# }

# .slider:before {
#   position: absolute;
#   content: "";
#   height: 26px;
#   width: 26px;
#   left: 4px;
#   bottom: 4px;
#   background-color: white;
#   -webkit-transition: .4s;
#   transition: .4s;
# }

# input:checked + .slider {
#   background-color: #2196F3;
# }

# input:focus + .slider {
#   box-shadow: 0 0 1px #2196F3;
# }

# input:checked + .slider:before {
#   -webkit-transform: translateX(26px);
#   -ms-transform: translateX(26px);
#   transform: translateX(26px);
# }

# /* Rounded sliders */
# .slider.round {
#   border-radius: 34px;
# }

# .slider.round:before {
#   border-radius: 50%;
# }
# </style>





    # <p style="color: rgb(255,255,255)">hidup kan merah?</p>
    # <label style="margin-left:20%;" class="switch">
    # <input class="merah" type="checkbox">
    # <span class="slider round" onclick='{if(!(document.querySelector(".merah").checked)){
    #     fetch("http:\/\/127.0.0.1:5000/yes/12", {method: "GET"})
    #     }
    #     else{
    #     fetch("http:\/\/127.0.0.1:5000/yes/21", {method: "GET"})
    #     }
    #     }'></span>
    # </label>
# {fetch("http://127.0.0.1:5000/yes/"+input.value, {method: "GET"})}}
@app.route('/yes/<data>', methods=['GET', 'POST'])
def ubah(data):
    content = request.json
    # content = json.loads(content)
    # content = jsonify(content)
    print(content["Temperature"])
    f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/arduino/posttest4/data.txt", "w")
    f.write(f"{content}")
    f.close()
    return jsonify({"lol":"ya"})


@app.route('/led1/<ku>', methods=['GET', 'POST'])
def led1(ku):
    f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/arduino/posttest4/led1.txt", "r")
    # f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/data.txt", "r")
    # print(f.readline())
    return f.readline()

@app.route('/led2/<ku>', methods=['GET', 'POST'])
def led2(ku):
    f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/arduino/posttest4/led2.txt", "r")
    # print(f.readline())
    # f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/data.txt", "r")
    return f.readline()

@app.route('/led3/<ku>', methods=['GET', 'POST'])
def led3(ku):
    f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/arduino/posttest4/led3.txt", "r")
    # print(f.readline())
    # f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/data.txt", "r")
    return f.readline()

@app.route('/data/<ku>', methods=['GET', 'POST'])
def datas(ku):
    f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/led.txt", "r")
    return jsonify({"data":f"2"})


# @app.route("/terang/<data>", methods=['GET', 'POST'])
# def data_terang(data):
#     f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/terang.txt", "w")
#     f.write(f"{data}")
#     f.close()
#     return jsonify({"lol":"ya"})

# @app.route("/nyaring/<data>", methods=['GET', 'POST'])
# def data_nyaring(data):
#     f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/nyaring.txt", "w")
#     f.write(f"{data}")
#     f.close()
#     return jsonify({"lol":"ya"})

# @app.route("/nyaring", methods=['GET', 'POST'])
# def nyaring():
#     f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/nyaring.txt", "r")
#     # f.write(f"{}")
#     return jsonify({"data":f"{f.read()}"})

# @app.route("/terang", methods=['GET', 'POST'])
# def terang():
#     f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/terang.txt", "r")
#     # f.write(f"{}")
#     return jsonify({"data":f"{f.read()}"})

# @app.route('/yes1/<data>')
# def ubah(data):
#     f = open("C:/Users/Alienware M17/Desktop/coding/server nonton anime/data1.txt", "w")
#     f.write(f"{data}")
#     f.close()
#     return jsonify({"lol":"ya"})


if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=5000,debug=True)