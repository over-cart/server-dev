from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = "mysecret"

# socket_io = SocketIO(app)

from app.routes import *