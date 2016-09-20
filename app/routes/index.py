# -*-coding:utf-8-*-
# from app import app, socket_io
from app import app
from flask import render_template, jsonify, request
from subprocess import call
from flask_socketio import send
from datetime import datetime
from MySql_connector import connector
import json

@app.route('/')
def index():
    return render_template('index-overcart.html')

@app.route('/overcart/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        param_id = request.form['id']
        print(param_id)
        if param_id == 'admin':
            tmp = render_template('admin-overcart.html')
        else:
            array_loc = [1,0,1,1,1,1, 0,1,0,0,1,0, 1,1,0,0,0,1, 1,0,1,0,0,1, 1,1,0,0,0,1, 0,1,1,1,0,0]
            tmp = render_template('user-overcart.html', array_loc=json.dumps(array_loc))

    return tmp


@app.route('/overcart/chat')
def chatting():
    return render_template('index-overcart.html')


# 카트의 움직임을 따라서 변화하는 정보를 받을 예정입니다 .
@app.route('/overcart/trace', methods=['GET', 'POST'])
def trace_cart():
    if request.method == 'GET':
        return "This is GET type Request, <br>Please do POST type in JSON format... "
    elif request.method == 'POST':
        value = request.json
        connector.insert_sign(value['rasp_id'],value['card_id'],value['datetime'])
        print(value)

        to_client = dict()
        to_client['response_time'] = datetime.now()
        to_client['rasp_id'] = value['rasp_id']
        to_client['card_id'] = value['card_id']
        return jsonify(to_client)


@app.route('/data')
def data():
    return jsonify({'hello': 'world', 'lee': 'junsu'})


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
