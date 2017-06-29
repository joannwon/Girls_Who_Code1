from PIL import Image

#FUNCTIONS
def darkBlue(pixel):
    newRed = 0
    newGreen = 51
    newBlue = 76
    p = ( newRed , newGreen, newBlue)
    newPixelList.append(p)
def red(pixel):
    newRed = 217
    newGreen = 26
    newBlue = 33
    p = ( newRed , newGreen, newBlue)
    newPixelList.append(p)
def lightBlue(pixel):
    newRed = 112
    newGreen = 150
    newBlue = 158
    p = ( newRed , newGreen, newBlue)
    newPixelList.append(p)
def yellow(pixel):
    newRed = 252
    newGreen = 227
    newBlue = 166
    p = ( newRed , newGreen, newBlue)
    newPixelList.append(p)



#Import the image and make pixel list
myImage = Image.open("weirdJoann.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

#pixel manipulation
for pixel in pixelList:
    red1 = pixel[0]
    green1 = pixel[1]
    blue1 = pixel[2]

    intensity = red1 + green1 + blue1
    

    if ( intensity < 182):
       darkBlue(pixel)

    elif (182 <= intensity<364):
       red(pixel)

    elif (364 <= intensity < 546):
       lightBlue(pixel)

    elif (intensity >= 546):
       yellow(pixel)



        
       




#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
newImage.save("newPhoto.bmp","bmp")

