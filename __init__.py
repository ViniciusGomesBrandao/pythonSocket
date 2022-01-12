from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO, emit
app = Flask(__name__)
api = Api(app)

socketio = SocketIO(app, cors_allowed_origins="*")
@socketio.on('connect', namespace='/balance')
def balance():
    print("Emiting Event")
    emit('event', { 'balance': 1 }, namespace='/balance')

@socketio.on('connect', namespace='/user')
def user():
    print("Emiting Event")
    emit('event', { 'evento': 'user' }, namespace='/user')
if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1', port=8080)
    