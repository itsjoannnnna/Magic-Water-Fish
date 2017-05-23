import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import picamera
import numpy
import time
import datetime
import os
import sys

s_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/build/lib/MWF/steelhead/data1/cascade.xml')

cap = cv2.VideoCapture('http://192.168.0.100:8080/stream.mjpg')

fps = cap.get(5)
height = cap.get(4)
width = cap.get(3)

print(fps)
print(height)
print(width)

def s_image_detection():
       
        #steelhead classifier
        print "steelhead"
        while(cap.isOpened()):
                ret, img = cap.read()
        
                if ret:
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        steelhead = s_cascade.detectMultiScale(gray, 1.3, 5)
                        for(x,y,w,h) in steelhead:
                                cv2.rectangle(img,(x,y), (x+w, y+h), (255, 255,0),2)
                                roi_gray = gray[y:y+h, x:x+w]
                                roi_color = img[y:y+h, x:x+w]

                        cv2.imshow('img', img)
                        
                k = cv2.waitKey(10) & 0xff
                #k = cv2.waitKey(10)
                if k == 27:
                        break

##        cv2.destroyAllWindows() 
##        cv2.VideoCapture(0).release()  
        cap.release()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    s_image_detection()
