from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY_DESAFIO_03'
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    socketio.send(message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
