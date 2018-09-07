#!/usr/bin/env python2

import picamera
from flask import Flask
from io import BytesIO
import time

app = Flask(__name__)

camera = picamera.PiCamera()
camera.resolution = (800,600)

myStream = BytesIO()


@app.route("/")
def index():
    camera.start_preview()
    time.sleep(2)
    camera.capture(myStream, 'jpeg')
    return send_file(myStream, mimetype='image/gif')

@app.route('/test')
def test():
	return 'raspi and flask running;'



if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)