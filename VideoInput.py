
######################### Video Input from Raspberry Pi Camera Module#####################
#REFERENCE: pyimagesearch.com

# First of all we need to import neccessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
# resolution of the camera
camera.resolution = (640, 480)
# Frames per second
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
# Actual video stream is captured by calling the capture_continuous function
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	# show the frame
	cv2.imshow("Frame", image)
	#0xFF is the hexadecimal constant
	key = cv2.waitKey(1) & 0xFF
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break