from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:

joe = Turtle()

joe.pen(pensize=5)


def drawShape(sides):
    direction = 360/sides
    drawnsides = 0
    while drawnsides < sides:
        joe.pendown()
        joe.forward(100)
        joe.penup()
        joe.left(direction)
        drawnsides += 1
print("What color?")
color = input()

joe.pen(pencolor = color)

print("How many sides?")
sides = int(input())
    
drawShape(sides)
print("Again? Type y for yes and n for no")
answer = input()
 

while answer == "y":
    joe.clear()
    print("What color?")
    color = input()

    joe.pen(pencolor = color)

    print("How many sides?")
    sides = int(input())
    
    drawShape(sides)
    print("Again?")
    answer = input()


if answer == "n":
        joe.clear()
        print("Bye.")





# Close window on click.
exitonclick()
