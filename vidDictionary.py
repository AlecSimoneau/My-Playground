import random
from makeVideo import oldSize, VidFrame

#random.seed(1)


#a binary from 0 to 100 to use as id's for pixels
ID_One = ['0', '1', '10', '11', '100', '101', '110', '111',  
        '1000', '1001', '1010', '1011', '1100', '1101',
        '1110', '1111', '10000', '10001', '10010', '10011',
        '10100', '10101', '10110', '10111', '11000', '11001',
        '11010', '11011', '11100', '11101', '11110', '11111',
        '100000', '100001', '100010', '100011', '100100',
        '100101', '100110', '100111', '101000', '101001',
        '101010', '101011', '101100', '101101', '101110',
        '101111', '110000', '110001', '110010', '110011',
        '110100', '110101', '110110', '110111', '111000',
        '111001', '111010', '111011', '111100', '111101',
        '111110', '111111', '1000000', '1000001', '1000010', 
        '1000011', '1000100', '1000101', '1000110', '1000111', 
        '1001000', '1001001', '1001010', '1001011', '1001100', 
        '1001101', '1001110', '1001111', '1010000', '1010001',
        '1010010', '1010011', '1010100', '1010101', '1010110', 
        '1010111', '1011000', '1011001', '1011010', '1011011', 
        '1011100', '1011101', '1011110', '1011111', '1100000',
        '1100001', '1100010', '1100011', '1100100']

#### User Variables ######
var = {}
placeholder = ""
##########################


# This loop takes the id's from ID_One and assigns them a random pixel position, and whether its an even or odd
# number, they get the designation 'red' or 'blue'
for id in ID_One:
    assert ((id[-1] == "1") or (id[-1] == "0")), "Impropper ID" ## Messing around with assert statements
    if id[-1] == "0":
        placeholder = "red"
    if id[-1] == "1":
        placeholder = "blue"
    
    ###### NEED TO CHANGE ######
    # posibiity for there to be overlap/same values to be generated so multiple ids have the same pixel position
    var.update({id: [[random.randint(0,oldSize[0]-1),random.randint(0,oldSize[1])-1], placeholder ]})

# Assigns FRAME_ONE the VidFrame class, and I don't need an individual pixel position
# Which is why i am passing in None, (throws an error otherwise)
FRAME_ONE = VidFrame(None)
# Making the frame
imageFrame = FRAME_ONE.makeFrame()

#This for loop takes the pixel position and color, 'red' or 'blue', for each id and 
# Draws them on the image that color
for id in ID_One:
    color = []
    assert (var.get(id)[1]  == "red" or var.get(id)[1] == "blue"), "Incorrect color id"
    if var.get(id)[1] == "red":
        color = [0,0,250]
    else:
        color = [250,0,0]    
    imageFrame[int(var.get(id)[0][0]),int(var.get(id)[0][1])] = color

# shows the image with the colored in pixels
FRAME_ONE.show("title",FRAME_ONE.upScale(5,imageFrame))



