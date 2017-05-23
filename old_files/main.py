import os

os.system("sudo modprobe bcm2835-v4l2")
os.system("v4l2-ctl --overlay=1")
os.system("v4l2-ctl --overlay=0")

from Tkinter import *
import Tkinter as tk
import tkFont
import sys
from cam import pic, video, livefeed
from chinook import c_image_detection
##from steelhead import s_image_detection
import cv2
##from gps import gps

#p = PhotoBoothApp()

root = Tk()
myFont = tkFont.Font(family = 'Helvetica', size=36, weight='bold') 
f = Frame(root, height = 1000, width = 1000)
f.pack_propagate(0) #don't shrink
f.pack()

def live():
    livefeed()

def c():
    c_image_detection()
##
##def s():
##    s_image_detection()
    
def exit():
    sys.exit()
    
##def take_pic():
##    pic()
##
##def take_video():
##    video()

##def coordinates():
##    gps()
##
##def reboot():
##    os.system("bash /home/pi/reboot.sh")
    
liveButton = Button(f, width = 10, height = 5, text = "LIVEFEED", command = live)
liveButton.pack()

cButton = Button(f, width = 10, height = 5, text = "CHINOOK", command = c)
cButton.pack()
##    
##sButton = Button(f, width = 10, height = 5, text = "STEELHEAD", command = s)
##sButton.pack()

##picButton = Button(f, width = 10, height = 5, text = "PICTURE", command = take_pic)
##picButton.pack()
##
##videoButton = Button(f, width = 10, height = 5, text = "VIDEO", command = take_video)
##videoButton.pack()
##
##coorButton = Button(f, width = 10, height = 5, text = "COORDINATES", command = coordinates)
##coorButton.pack()
##
##rebootButton = Button(f, width = 10, height = 5, text = "REBOOT", command = reboot)
##rebootButton.pack()

exitButton = Button(f, width = 10, height = 5, text = "QUIT", command = exit)
exitButton.pack()

root.geometry('125x600') #size of the window
root.geometry("+30+40") #moves the window
root.mainloop()
root.destroy()
