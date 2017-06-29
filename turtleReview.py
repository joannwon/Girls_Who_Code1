#importing libraries
from turtle import *
import math

#setting up screen size
setup(500,500)

#Functions
def whileDrawShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        turtle.forward(50)
        turtle.left(angle)
        drawnSides += 1
        
def forDrawShape(turtle,sides,color):
    turtle.pencolor(color)
    angle = 360/sides

    for s in range(sides):
        turtle.forward(50)
        turtle.left(angle)
        
#Running Code

joe = Turtle() #creates turtle
joe.turtlesize(2,2) #makes turtle larger
joe.pensize(2) #makes pen larger


another = True

while another == True:
    joe.pendown()
    
    print("How many sides?")
    numSides = int(input())

    print("What color?")
    chosenColor = input()

    forDrawShape(joe,numSides,chosenColor)

     print("Again?")
    answer = input()

    if (answer == "no"):
        another = False

    if (answer == "yes"):
        joe.penup()
        joe.forward(100)
        another = True
    
    


#whileDrawShape(joe,4,"green")
#joe.penup()
#joe.forward(100)
#joe.pendown()
#forDrawShape(joe,5,"pink")


#closes the turtle window on click
exitonclick()


