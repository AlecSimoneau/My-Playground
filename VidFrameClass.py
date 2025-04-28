import cv2 as cv
import numpy as np
import keyboard as kb
## VARS ##
pixPosition = []
oldSize = (127,127)
##########

class VidFrame():

    #Initializes with height, width and color channels 
    def __init__(self,pixPosition, height = oldSize[0], width = oldSize[1], channels = 3):
        self.height = height
        self.width = width
        self.channels = channels
        self.pixPosition = pixPosition
        
        
    
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
        
        # Keeps the window until you press a key
        cv.waitKey(0)

    def moveUp(self,im):
        pixPositionOld = self.pixPosition
        pixPositionNew = [int(pixPositionOld[0])+1,pixPositionOld[1]]
        im[pixPositionNew] = [255,255,255]
        im[pixPositionOld] = [0,0,0]
        print("Moved Up!")
        return im,pixPositionNew

    def moveDown(self,im):
        pixPositionOld = self.pixPosition
        pixPositionNew = [int(pixPositionOld[0])-1,pixPositionOld[1]]
        im[pixPositionNew] = [255,255,255]    
        im[pixPositionOld] = [0,0,0]    
        print("Moved Down!")
        return im,pixPositionNew

    def moveRight(self,im):
        pixPositionOld = self.pixPosition
        pixPositionNew = [pixPositionOld[0],int(pixPositionOld[1])+1]
        im[pixPositionOld] = [0,0,0]
        im[pixPositionNew] = [255,255,255]
        print("Moved Right!")
        return im,pixPositionNew

    def moveLeft(self,im):
        pixPositionOld = self.pixPosition
        pixPositionNew = [pixPositionOld[0],int(pixPositionOld[1])-1]
        im[pixPositionOld] = [0,0,0]
        im[pixPositionNew] = [255,255,255]
        print("Moved Left!")
        return im, pixPositionNew

    def center(self,im):
        pass

# Move logic

# pixel position
# move -> on([x + a , y + b]) = [x_new,y_new] & delete([x_old,y_old])
