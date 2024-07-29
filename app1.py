<<<<<<< HEAD
# server.py
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import cv2
import base64

app = Flask(__name__)
socketio = SocketIO(app)

cap = None
is_camera_running = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_frames():
    global cap, is_camera_running
    while is_camera_running:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@socketio.on('connect')
def handle_connect():
    global cap, is_camera_running
    if not is_camera_running:
        cap = cv2.VideoCapture(0)
        is_camera_running = True
        emit('camera_started')

@socketio.on('disconnect')
def handle_disconnect():
    global cap, is_camera_running
    if is_camera_running:
        cap.release()
        is_camera_running = False

if __name__ == '__main__':
    socketio.run(app, debug=True)
=======
# server.py
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import cv2
import base64

app = Flask(__name__)
socketio = SocketIO(app)

cap = None
is_camera_running = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_frames():
    global cap, is_camera_running
    while is_camera_running:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@socketio.on('connect')
def handle_connect():
    global cap, is_camera_running
    if not is_camera_running:
        cap = cv2.VideoCapture(0)
        is_camera_running = True
        emit('camera_started')

@socketio.on('disconnect')
def handle_disconnect():
    global cap, is_camera_running
    if is_camera_running:
        cap.release()
        is_camera_running = False

if __name__ == '__main__':
    socketio.run(app, debug=True)
>>>>>>> d80cad45c4a01c03a2b296e3e232691c658d7a1d
