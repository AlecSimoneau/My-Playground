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

    def moveDown(self,im,scaleFactor):
        self.upScale(-1*scaleFactor,im)
        im[self.pixPosition[0], self.pixPosition[1]] = [0,0,0]
        pixPositionNew = [int(self.pixPosition[0])+1,int(self.pixPosition[1])]
        im[pixPositionNew[0],pixPositionNew[1]] = [0,0,255]
        self.pixPosition = pixPositionNew
        return self.show("title",self.upScale(scaleFactor,im))

    def moveUp(self,im,scaleFactor):
        self.upScale(-1*scaleFactor,im)
        im[self.pixPosition[0], self.pixPosition[1]] = [0,0,0]  
        pixPositionNew = [int(self.pixPosition[0])-1,int(self.pixPosition[1])]
        im[pixPositionNew[0],pixPositionNew[1]] = [0,0,255]  
        self.pixPosition = pixPositionNew  
        return self.show("title",self.upScale(scaleFactor,im))

    def moveRight(self,im,scaleFactor):
        self.upScale(-1*scaleFactor,im)
        im[self.pixPosition[0], self.pixPosition[1]] = [0,0,0]
        pixPositionNew = [int(self.pixPosition[0]),int(self.pixPosition[1])+1]
        im[pixPositionNew[0],pixPositionNew[1]] = [0,0,255]
        self.pixPosition = pixPositionNew
        return self.show("title",self.upScale(scaleFactor,im))
        

    def moveLeft(self,im,scaleFactor):
        self.upScale(-1*scaleFactor,im)
        im[self.pixPosition[0], self.pixPosition[1]] = [0,0,0]
        pixPositionNew = [int(self.pixPosition[0]),int(self.pixPosition[1])-1]
        im[pixPositionNew[0],pixPositionNew[1]] = [0,0,255]
        self.pixPosition = pixPositionNew
        return self.show("title",self.upScale(scaleFactor,im))
