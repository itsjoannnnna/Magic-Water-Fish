import sys
import os
import cv2
import picamera
import numpy as np
import time
import datetime
import PyQt4
from PyQt4 import QtGui, QtCore
import urllib
                                                                                                                                                                                                                   #cascade classifier for chinook salmon
c_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/build/lib/MWF/chinook/data/cascade.xml')
#cascade classifier for steelhead salmon
s_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/build/lib/MWF/steelhead/data1/cascade.xml')

class video(QtGui.QWidget):
        def __init__(self, *args):
                super(QtGui.QWidget, self).__init__()
                self.cap = cv2.VideoCapture(-1)
                self.vid_frame = QtGui.QLabel()
                lay = QtGui.QVBoxLayout()
                lay.setMargin(0)
                
                lay.addWidget(self.vid_frame)
                self.setLayout(lay)
                
                #checks to see that camera has been turned on
                fps = self.cap.get(5)
                height = self.cap.get(4)
                width = self.cap.get(3)

                print(fps)
                print(height)
                print(width)

        def c_detection(self):
                #print "video 2"
                #chinook 
                while(self.cap.isOpened()):
                        ret, img = self.cap.read()
                
                        if ret:
                                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                #detectMultiScale(image, scaleFactor, minNeighbors)
                                chinook = c_cascade.detectMultiScale(gray, 1.3, 5)
                                for(x,y,w,h) in chinook:
                                        cv2.rectangle(img,(x,y), (x+w, y+h), (255, 255,0),2)
                                        roi_gray = gray[y:y+h, x:x+w]
                                        roi_color = img[y:y+h, x:x+w]

                                cv2.imshow('chinook', img)
                        #press q to close opencv window
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                                break

                self.cap.release()
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                
        def s_detection(self):
                while(self.cap.isOpened()):
                        ret, img = self.cap.read()
                
                        if ret:
                                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                steelhead = s_cascade.detectMultiScale(gray, 1.3, 5)
                                for(x,y,w,h) in steelhead:
                                        cv2.rectangle(img,(x,y), (x+w, y+h), (255, 255,0),2)
                                        roi_gray = gray[y:y+h, x:x+w]
                                        roi_color = img[y:y+h, x:x+w]

                                cv2.imshow('steelhead', img)
                        #press q to close opencv window
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                                break

                self.cap.release()
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                
        def reboot(self):
                cv2.destroyAllWindows()
                self.cap.release()
                os.system("bash /home/pi/reboot.sh")

        def quitCapture(self):
                print "pressed quit"
                cv2.destroyAllWindows()
                self.cap.release()
                QtCore.QCoreApplication.quit()

class ControlWindow(QtGui.QWidget):
        def __init__(self):
                QtGui.QWidget.__init__(self)

                
                #declares the functions for the buttons
                self.capture = video()
                self.sdetect_button = QtGui.QPushButton('Steelhead',self)
                self.sdetect_button.clicked.connect(self.capture.s_detection)
                self.sdetect_button.setFixedWidth(100)                

                self.cdetect_button = QtGui.QPushButton('Chinook',self)
                self.cdetect_button.clicked.connect(self.capture.c_detection)
                self.cdetect_button.setFixedWidth(100)
                
                self.quit_button = QtGui.QPushButton('Quit',self)
                self.quit_button.clicked.connect(self.capture.quitCapture)
                self.quit_button.setFixedWidth(100)
                
                self.reboot_button = QtGui.QPushButton('Refresh',self)
                self.reboot_button.clicked.connect(self.capture.reboot)
                self.reboot_button.setFixedWidth(100) 
                
                vbox = QtGui.QVBoxLayout(self)
                vbox.addWidget(self.quit_button)
                vbox.addWidget(self.reboot_button)
                vbox.addWidget(self.cdetect_button)
                vbox.addWidget(self.sdetect_button)
                
                self.setLayout(vbox)
                self.setGeometry(28,66,600,100)
                self.show()
                
if __name__ == '__main__':
        import sys
        app = QtGui.QApplication(sys.argv)
        window = ControlWindow()
        #window name
        window.setWindowTitle("Menu")
        #resizing the entire window
        window.resize(769, 413)
        sys.exit(app.exec_())
