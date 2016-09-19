# from app import app, socket_io
from app import app
from flask import render_template, jsonify, request
from subprocess import call
from flask_socketio import send


@app.route('/')
def index():
    return render_template('index-overcart.html')

@app.route('/overcart/')
def hello_world():
    return "Hello OverCart Project Home Page!!"

@app.route('/overcart/chat')
def chatting():
    return render_template('index-overcart.html')

# 카트의 움직임을 따라서 변화하는 정보를 받을 예정입니다 .
@app.route('/overcart/trace', methods=['GET', 'POST'])
def trace_cart():
    if request.method == 'GET':
        return "This is GET type Request"
    elif request.method == 'POST':
        value = request.json
        print(value)
        return value['name']

@app.route('/data')
def data():
    return jsonify({'hello':'world', 'lee':'junsu'})

@app.route('/others')
def others():
    value = call(['python', 'others/stock_program.py'])
    print(value)
    return "other program run in background"

# @socket_io.on("hello")
# def hello(message):
#     print(">>Hello : ", message)
#     send(message, broadcast=True)
#
#
# @socket_io.on("message")
# def request(message):
#     print("message : "+ message)
#     to_client = dict()
#     if message == 'new_connect':
#         to_client['message'] = "새로운 유저가 난입하였다!!"
#         to_client['type'] = 'connect'
#     else:
#         to_client['message'] = message
#         to_client['type'] = 'normal'
#     # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
#     send(to_client, broadcast=True)