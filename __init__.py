
from flask import Flask
from flask_restful import Api, Resource
from flask_socketio import SocketIO, emit, namespace
from balance import Balance
import time


app = Flask(__name__)
api = Api(app)

socketio = SocketIO(app, cors_allowed_origins="*")
socketio.on_namespace(Balance('/balance'))
class Index(Resource):
    def get(self):
        socketio.emit('event', {"balance": 2}, namespace="/balance")
        return {'success': True}
api.add_resource(Index, '/')
if __name__ == '__main__':
    
    socketio.run(app,host='127.0.0.1', port=8080)
    


