from flask_socketio import Namespace, emit
class Balance(Namespace):
    def on_connect(self):
        emit('event', { 'evento': 'connect' })
        
    def on_disconnect(self):
        emit('event', { 'evento': 'disconnect' })

    def on_active(self, data):
        emit('event', {"balance": 2})