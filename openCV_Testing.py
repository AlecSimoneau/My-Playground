## This file is a test to see if i can create multiple images, store them, and play them as a video
import cv2 as cv
import numpy as np


## I want to make a class to assign the same attributes to each window
## The attributes i want to assign are width, height and channels
## I'm not sure the best way to do this so...
class VidFrame:
    
    ## I tried __init__ but it didn't work the way i wanted?

    #def __init__(self, height, width, channels,frame):
    #self.height = height
    #self.width = width
    #self.channels = channels
    #self.frame - frame
        
    ## I'm using the library openCV to create the images, and I want to assign an object the atribute frame,
    ## and have the frame have atributes height, width and channels
    def frame(self,height = 15,width = 15,channels = 3):
        self.height = height
        self.width = width
        self.channels = channels

    ## This is to scale up the image, to reduce the initail amount of pixels i work with
    ## It works so thats good
    def upScale(scaleFactor,frame):
        bigFrame = cv.resize(frame,(frame.height * scaleFactor, frame.width * scaleFactor))

    ## This just makes a window with a 'title' and puts the image 'frame' in it
    def show(title, frame):
        cv.imshow(title, VidFrame.frame)
        # Keeps the window until you press a key
        cv.waitKey(0)

# assigns p1 to the VidFrame class
p1 = VidFrame()

##### This makes an image but here is where it breaks
## the p1.frame.xxxx doesn't work, it says that frame doesn't have the atribute height?
## I just need to recover height, width and channels from def frame(), but there's probably a better way to do this

p1.frame() = np.zeros((p1.frame.height,p1.frame.width,p1.frame.channels),np.uint8)

####

# Makes the image bigger
p1.upScale(10,p1.frame)

# Calls the function to create the window
p1.show("Title",p1.frame)
