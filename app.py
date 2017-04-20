import turtle
import random

def coinToss():
    return random.randrange(0,2)

def randomTurn():
    return random.randrange(0,91)

def moveTurtle(turtle, step):
    direction = coinToss()
    if direction == 0:
        turtle.right(randomTurn())
    else:
        turtle.left(randomTurn())
    turtle.forward(step)

def isOnScreen(window,turtle):
    leftBound = -(window.window_width() / 2)
    rightBound = window.window_width() / 2
    topBound = window.window_height() / 2
    bottomBound = -(window.window_height() / 2)

    turtleX = turtle.xcor()
    turtleY = turtle.ycor()

    exit_x = True
    exit_y = True
    if turtleX > rightBound or turtleX < leftBound:
        exit_x = False
    if turtleY > topBound or turtleY < bottomBound:
        exit_y = False

    return exit_y and exit_x

# setting window size to avoid 0.5 that is messy on dual monitor setup

window = turtle.Screen()
window_height = 600
window_width = 1000
window.setup(window_width, window_height)

fiat = turtle.Turtle()
skoda = turtle.Turtle()

fiat.color("green")
fiat.speed(10)
skoda.color("blue")
skoda.speed(10)

while isOnScreen(window,fiat) and isOnScreen(window, skoda):
    moveTurtle(fiat, 30)
    moveTurtle(skoda, 30)

window.exitonclick()
