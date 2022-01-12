
from flask import Flask
from flask_restful import Api, Resource
from flask_socketio import SocketIO, emit
from threading import Thread
from time import sleep
import requests
app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins="*")
class Index(Resource):
    def get(self):
        socketio.emit('event', {"balance": 2}, namespace="/balance")
        return {'success': True}
api.add_resource(Index, '/')
def startServer():
    socketio.run(app,host='127.0.0.1', port=8080)
def loopRequest():
    sleep(4)
    while True:
        sleep(1)
        requests.get("http://127.0.0.1:8080")
if __name__ == '__main__':
    server = Thread(target = startServer).start()
    loop = Thread(target = loopRequest).start()
