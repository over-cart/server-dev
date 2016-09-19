from app import app, socket_io
from flask import render_template, jsonify
from subprocess import call
from flask_socketio import send


@app.route('/')
def index():
    return "index"

@app.route('/overcart/')
def hello_world():
    return "Hello Gaemigo Project Home Page!!"

@app.route('/overcart/chat')
def chatting():
    return render_template('chat2.html')

@app.route('/data')
def data():
    return jsonify({'hello':'world', 'lee':'junsu'})

@app.route('/others')
def others():
    value = call(['python', 'others/stock_program.py'])
    print(value)
    return "other program run in background"

@socket_io.on("hello")
def hello(message):
    print(">>Hello : ", message)
    send(message, broadcast=True)


@socket_io.on("message")
def request(message):
    print("message : "+ message)
    to_client = dict()
    if message == 'new_connect':
        to_client['message'] = "새로운 유저가 난입하였다!!"
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
    send(to_client, broadcast=True)