from picamera import PiCamera
from time import sleep
camera =PiCamera()
# camera.rotation = 180 # Rotate Camera 180 degrees
# camera.resolution = (640, 480) # Set a resolution
# Max(2592,1944), Min(64, 64)
# camera.framerate = 15
# camera.annotate_text = "Hello" # Annotation text
# camera.annotate_text_size = 50
# camera.brightness = 50 # Brightnes Default: 50
# Value range - (0->100)
# # Perform preview if GUI is available
# camera.start_preview()
# Take a capture of 3 images.
for i in range(3):
# Sleep allows camera sensor to sense the light level.
sleep(2)
camera.capture('/home/pi/py-image%s.jpg' % i)
# camera.stop_preview()
# Record a video
camera.start_recording('/home/pi/py-video.h264')
sleep(5)
camera.stop_recording()