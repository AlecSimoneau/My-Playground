## This file is a test to see if i can create multiple images, store them, and play them as a video
import cv2 as cv
import numpy as np
from VidFrameClass import VidFrame
import keyboard as kb
################ USER VARIABLES #########################

#temp iteratable
j = 1 
oldSize = (127,127)
pixPosition = [oldSize[0]//2 , oldSize[1]//2]
output = None
############## END USER VARIABLES #######################


#This class allows me to make, resize and show an image with relative ease
i = VidFrame()

#makes a frame
im = i.makeFrame()

#Colors a single pixel in the center
im[int((i.height / 2) - 1),int((i.width / 2) - 1)] = [0,0,255]

#Makes the frame 10x larger from the default and shows it
i.show("title",i.upScale(10,im)) 


# A while loop that takes key intputs 
# Intended to move the pixel around based on the arrow keys until the user hits the esc key
# Upon which the loop will break and the windows will be closed
while True:
    keyEvent = str(kb.read_event())
    print(keyEvent)

    #The output of the keyboard function read_event() is 
    # KeyboardEvent(pressedKey up/down)
    # A compare statement seemed like the simplest way to do this for pure functionality
    # I may make this prettier in the future

    #These compare statements are supposed to move the pixel but it is still
    # a work in progress
    if keyEvent == 'KeyboardEvent(right up)':
        i.show("title",i.upScale(-10,im))
        i.moveRight(im)
        i.show("title",i.upScale(10,im))
    if keyEvent == 'KeyboardEvent(left up)':
        i.show("title",i.upScale(-10,im))
        i.moveLeft(im)
        i.show("title",i.upScale(10,im))
    if keyEvent == 'KeyboardEvent(up up)':
        i.show("title",i.upScale(-10,im))
        i.moveUp(im)
        i.show("title",i.upScale(10,im))
    if keyEvent == 'KeyboardEvent(down up)':
        i.show("title",i.upScale(-10,im))
        i.moveDown(im)
        i.show("title",i.upScale(10,im))
      
    #Breaks the loop when esc is presed
    if keyEvent == 'KeyboardEvent(esc up)':
        cv.destroyAllWindows()
        break    
