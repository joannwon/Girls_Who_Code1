from PIL import Image

#Import the image

myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList= []

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]


#EXPOSURE        
##    newRed = red*2
##    if newRed > 255:
##        newRed = 255
##        
##    newGreen = green*2
##    if newGreen > 255:
##        newGreen = 255
##        
##    newBlue = blue*2
##    if newBlue > 255:
##        newBlue = 255


    
#BLACK AND WHITE
##    avg = (red + green + blue)//3
##    newRed = avg
##    newGreen = avg
##    newBlue = avg
##        
##    p = (newRed,newGreen,newBlue)
##
##    #add pixel to new pixel list
##    newPixelList.append(p)



#NEGATIVE
    newRed = 255 - red

    newGreen = 255 - green

    newBlue = 255 - blue

    p = (newRed,newGreen,newBlue)

#open image
newImage = Image.new("RGB", myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.save("newPhoto.jpeg","jpeg")
