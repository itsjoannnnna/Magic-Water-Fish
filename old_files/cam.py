from Tkinter import *
import Tkinter as tk
import tkFont
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from time import sleep
import cv2
import os
import numpy
import io
import datetime

camera = PiCamera()
camera.resolution = (720, 480)
camera.framerate = 15

def livefeed():
    root = Tk()
    myFont = tkFont.Font(family = 'Helvetica', size=36, weight='bold') 
    f = Frame(root, height = 1000, width = 1000)
    f.pack_propagate(0) #don't shrink
    f.pack()
    
    pid = os.getpid()
    print(pid)
    my_stream = io.BytesIO()
    camera.start_preview()
    time.sleep(2)
    camera.capture(my_stream, 'jpeg')
    def exit():
        camera.close()
        os.system("bash /home/pi/reboot.sh")
        
    exitButton = Button(f, width = 10, height = 5, text = "EXIT LIVEFEED", command = exit)
    exitButton.pack()

    root.geometry('125x100') #size of the window
    root.geometry("+30+40") #moves the window
    root.mainloop()
    root.destroy()

def pic():
    pid = os.getpid()
    print(pid)
    camera.start_preview()
    i = 0
    while os.path.exists("/home/pi/Desktop/Fish_Feed/image%s.jpg" % i):
        i += 1

    sleep(1)
    camera.capture("/home/pi/Desktop/Fish_Feed/image%s.jpg" % i)
    camera.stop_preview()
    
def video():
    pid = os.getpid()
    print(pid)
    camera.start_preview()
    j = 0
    while os.path.exists("/home/pi/Desktop/Fish_Feed/video%s.h264" % j):
        j+=1
        
    camera.start_recording("/home/pi/Desktop/Fish_Feed/video%s.h264" % j)
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()

##if __name__ == '__main__':
##    globals()[sys.argv[1]]()
