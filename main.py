import os
from Tkinter import *
import Tkinter as tk
import tkFont
import sys
import chinook
import cv2

#p = PhotoBoothApp()

root = Tk()
myFont = tkFont.Font(family = 'Helvetica', size=36, weight='bold') 
f = Frame(root, height = 1000, width = 1000)
f.pack_propagate(0) #don't shrink
f.pack()

def c():
    chinook.main()
    
def reboot():
    os.system("bash /home/pi/reboot.sh")
    
def exit():
    sys.exit()

cButton = Button(f, width = 10, height = 5, text = "DETECTION", command = c)
cButton.pack()

rebootButton = Button(f, width = 10, height = 5, text = "REBOOT", command = reboot)
rebootButton.pack()

exitButton = Button(f, width = 10, height = 5, text = "QUIT", command = exit)
exitButton.pack()

root.geometry('125x300') #size of the window
root.geometry("+30+40") #moves the window
root.mainloop()
root.destroy()
