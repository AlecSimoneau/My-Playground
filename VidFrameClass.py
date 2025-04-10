import cv2 as cv
import numpy as np
import keyboard as kb
## VARS ##

#temp iteratable
j = 1 

pixX = None
pixY = None
pixPosition = [pixX,pixY]
oldSize = (127,127)
##########

class VidFrame():

    #Initializes with height, width and color channels 
    def __init__(self, height = oldSize[0], width = oldSize[1], channels = 3,pixX, pixY, pixPosition):
        self.height = height
        self.width = width
        self.channels = channels
        self.pixX = pixX
        self.pixY = pixY
        pixPosition = [pixX,pixY]
    
    # this should make a black image with the atributes height, width and channels
    def makeFrame(self):
        im = np.zeros((self.height,self.width,self.channels),np.uint8)    
        return im
                
    ## This is to scale up the image, to reduce the initail amount of pixels i work with
    ## It works so thats good
    def upScale(self,scaleFactor,name):
        if scaleFactor > 0:
            self.height = self.height * scaleFactor
            self.width = self.width * scaleFactor
            return cv.resize(name,(self.height, self.width),interpolation = cv.INTER_LINEAR_EXACT)
        elif scaleFactor < 0:
            self.height = self.height // (scaleFactor * -1)
            self.width = self.width // (scaleFactor * -1)
            return cv.resize(name,(self.height, self.width),interpolation = cv.INTER_LINEAR_EXACT)
        else:
            return name
        

    ## This just makes a window with a 'title' and puts the image 'frame' in it
    def show(self,title: str,name):#,delay):
        cv.imshow(title,name)
    
    
    ### When called I want the following four functions to update the pixel position to one pixel adjacent to the original position
    def moveRight(self,im,pixPositon):

        pixPositionOld = pixPosition
        pixPositionNew = [pixPosition[0]+1,pixPosition[1]]
        im[pixPositionNew] = [255,255,255]
        im[pixPositionOld] = [0,0,0]
        print("Moved Right!")

    def moveLeft(self,im):
        pixPositionOld = pixPosition
        pixPositionNew = [pixX-1,pixY]
        im[pixPositionNew] = [255,255,255]        
        print("Moved Left!")
        
    def moveUp(self,im):
        pixPositionOld = pixPosition
        pixPositionNew = [pixX,pixY+1]
        im[pixPositionNew] = [255,255,255]
        print("Moved Up!")
        
    def moveDown(self,im):
        pixPositionOld = pixPosition
        pixPositionNew = [pixX,pixY-1]
        im[pixPositionNew] = [255,255,255]
        print("Moved Down!")
    ###
    
    ## This is where I might center the pixel, but I want to solve the above functions first
    def center(image):
        pass


# Move logic

# pixel position
# move -> on([x + a , y + b]) = [x_new,y_new] & delete([x_old,y_old])
