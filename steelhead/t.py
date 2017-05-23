import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import picamera
import numpy
import time
import datetime

#chinook classifier
c_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/build/lib/MWF/chinook/data/cascade.xml')

#steelhead classifier
s_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/build/lib/MWF/steelhead/data1/cascade.xml')

cap = cv2.VideoCapture(1)

fps = cap.get(5)
height = cap.get(4)
width = cap.get(3)

print(fps)
print(height)
print(width)

def c_image_detection():
        print "chinook"
        while(cap.isOpened()):
                ret, img = cap.read()
        
                if ret:
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        chinook = c_cascade.detectMultiScale(gray, 1.3, 5)
                        for(x,y,w,h) in chinook:
                                cv2.rectangle(img,(x,y), (x+w, y+h), (255, 255,0),2)
                                roi_gray = gray[y:y+h, x:x+w]
                                roi_color = img[y:y+h, x:x+w]

                        cv2.imshow('img', img)
                        
                        k = cv2.waitKey(30) & 0xff
                        if k == 27:
                                break

        cap.release()
        cv2.destroyAllWindows()

def s_image_detection():
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
                        
                        k = cv2.waitKey(30) &0xff
                        if k == 27:
                                break

        cap.release()
        cv2.destroyAllWindows()   
