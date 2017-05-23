import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/gi')

import Gtk as Gtk


win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

##import sys
##sys.path.append('/usr/local/lib/python2.7/site-packages')
##import cv2
##import picamera
##import numpy
##import time
##import datetime
##import os
##import cv2
##
##print "starting"
##
##cam = cv2.VideoCapture(0)
##
##fps = cam.get(5)
##height = cam.get(4)
##width = cam.get(3)
##
##print(fps)
##print(height)
##print(width)
##
##def livefeed():
##    print "livefeed"
##    while(cam.isOpened()):
##        print "while"
##        ret, img = cam.read()
##        if ret:
##            img = cv2.flip(img, 1)
##        cv2.imshow('Webcam', img)
##        if cv2.waitKey(1) == 27:
##            break
##    cv2.destroyAllWindows
##
##def video():
##    print "video"
##    while(cam.isOpened()):
##        print "while"
##        ret, frame = cam.read()
##        if ret:
##            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##        cv2.imshow('frame',gray)
##        if cv2.waitKey(1) & 0xFF == ord('q'):
##            break
##    cap.release()
##    cv2.destroyAllWindows()
##
##if __name__ == '__main__':
##    globals()[sys.argv[1]]()
