## This file is a test to see if i can create multiple images, store them, and play them as a video
import cv2 as cv
#import numpy as np
from VidFrameClass import VidFrame
import keyboard as kb

################ USER VARIABLES #########################
oldSize = (127,127)
pixPosition = [int(oldSize[0]//2) , int(oldSize[1]//2)]
output = None
scaleFactor = 5
############## END USER VARIABLES #######################


#This class allows me to make, resize and show an image with relative ease
i = VidFrame(pixPosition)

#makes a frame
im = i.makeFrame()

#Colors a single pixel in the center
im[pixPosition[0],pixPosition[1]] = [0,0,255]

#Makes the frame larger by a scale factor from the default and shows it
i.show("title",i.upScale(scaleFactor,im)) 



# A while loop that takes key intputs 
# Intended to move the pixel around based on the arrow keys until the user hits the esc key
# Upon which the loop will break and the windows will be closed
while True:
    keyEvent = str(kb.read_event())
    temp = []
    #The output of the keyboard function read_event() is 
    # KeyboardEvent(pressedKey up/down)
    # A compare statement seemed like the simplest way to do this for pure functionality
    # I may make this prettier in the future
    
    
    if keyEvent == 'KeyboardEvent(right up)':
        i.moveRight(im,scaleFactor)

    if keyEvent == 'KeyboardEvent(left up)':
        i.moveLeft(im,scaleFactor)

    if keyEvent == 'KeyboardEvent(up up)':
        i.moveUp(im,scaleFactor)
        
    if keyEvent == 'KeyboardEvent(down up)':
        i.moveDown(im,scaleFactor)
        
      
    #Breaks the loop when esc is presed
    if keyEvent == 'KeyboardEvent(esc up)':
        print("Exited")
        cv.destroyAllWindows()
        break    
    cv.waitKey(10)
    



