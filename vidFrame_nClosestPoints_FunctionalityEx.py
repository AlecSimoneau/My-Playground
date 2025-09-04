from vidFrame import VidFrame, oldSize
im = VidFrame()
points = []
image,_ = im.makeFrame(numOfPixels=15,color=[0,250,0])
image,_ = im.makeFrame(numOfPixels=120,color=[255,0,0])
image,_ = im.makeFrame(numOfPixels=30,color = [10,10,150])
im.closestPoints(image=image,Point="Any",closestNPoints=65,show=True,scaleFactor=2)
