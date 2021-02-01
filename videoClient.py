import cv2
import socketio #python-socketio by @miguelgrinberg
import base64

sio = socketio.Client()
sio.connect('hhtp://172.20.10.4:3002')

cam = cv2.VideoCapture(0)

while (True):
  ret, frame = cam.read()                     # get frame from webcam
  res, frame = cv2.imencode('.jpg', frame)    # from image to binary buffer
  data = base64.b64encode(frame)              # convert to base64 format
  sio.emit('response', data)                      # send to server

cam.release()
