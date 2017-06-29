from PIL import Image

#FUNTIONS
def blackWhite(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    avg = (red + green + blue)//3
    newRed = avg
    newGreen = avg
    newBlue = avg

    p = (newRed,newGreen,newBlue)
    newPixelList.append(p)

def negative(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    newRed = 255 - red

    newGreen = 255 - green

    newBlue = 255 - blue

    p = (newRed,newGreen,newBlue)
    newPixelList.append(p)

def overExposure(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    newRed = red*2
    if newRed > 255:
        newRed = 255
        
    newGreen = green*2
    if newGreen > 255:
        newGreen = 255
        
    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)
    newPixelList.append(p)
    
def moreRed(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    newRed = red*2
    if newRed > 255:
        newRed = 255
    p = (newRed,green,blue)
    newPixelList.append(p)

def moreBlue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255
    p = (red,green,newBlue)
    newPixelList.append(p)
    
#RUNNING CODE
#Import the image and make pixel list
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)
#halfway = length // 2
oneThird = (length) // 3
twoThird = (2*(length))//3
threeThird = length

counter = 0    
    #pixel manipulation
for pixel in pixelList:
    
    counter += 1
    if (counter < oneThird): #one third of photo        
        moreRed(pixel)
    elif (oneThird<=counter<twoThird): #two third of photo
        blackWhite(pixel)
    elif(twoThird<=counter<threeThird): #three third of photo
        moreBlue(pixel)
    


#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.save("newPhoto.jpeg","jpeg")
