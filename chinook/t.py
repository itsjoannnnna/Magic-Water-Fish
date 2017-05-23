import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/build/lib/MWF/chinook/data/cascade.xmldata/cascade.xml')

img = cv2.imread('c.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

car = car_cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h) in car:
	cv2.rectangle(img,(x,y), (x+w, y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


##import cv2
##import sys
##
##cascade = cv2.CascadeClassifier('data/cascade.xml')
##
##video_capture = cv2.VideoCapture(0)
##
##while True:
##        ret, frame = video_capture.read()
##        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##        fish = cascade.detectMultiScale(gray, 1.3, 5)
##        for (x,y,w,h) in fish:
##                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
##
##        cv2.imshow('Video', frame)
##        if cv2.waitKey(1) & 0xFF == ord('q'):
##                break
##video_capture.release()
##cv2.destroyAllWindows()

##from picamera.array import PiRGBArray
##from picamera import PiCamera
##import time
##from time import sleep
##import cv2
##import sys
##import os
##import numpy
##import io
##import numpy as np
##import cv2
##
##camera = PiCamera()
##camera.resolution = (1024, 768)
##camera.framerate = 24
##
##fish_cascade = cv2.CascadeClassifier('data/cascade.xml')
##
##my_stream = io.BytesIO()
##camera.start_preview()
##
##time.sleep(2)
##
##camera.capture(my_stream, 'jpeg')
##
##ret, img = cv2.VideoCapture().read()
##
##gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##
##fish = fish_cascade.detectMultiScale(gray, 1.3, 5)
##for(x,y,w,h) in fish:
##	cv2.rectangle(img,(x,y), (x+w, y+h),(255,0,0),2)
##	roi_gray = gray[y:y+h, x:x+w]
##	roi_color = img[y:y+h, x:x+w]
##
##cv2.imshow('img', img)
