import turtle
import random

def coinToss():
    return random.randrange(0,2)

def moveTurtle(turtle, step):
    direction = coinToss()
    if direction == 0:
        turtle.right(90)
    else:
        turtle.left(90)
    turtle.forward(step)

def isOnScreen(window,turtle):
    # minus step - so the turtle does not disappear. if it hits the wall, it is done
    leftBound = -(window.window_width() / 2)
    rightBound = window.window_width() / 2
    topBound = window.window_height() / 2
    bottomBound = -(window.window_height() / 2)
    print(leftBound, rightBound, topBound, bottomBound)

    turtleX = turtle.xcor()
    turtleY = turtle.ycor()

    exit_x = True
    exit_y = True
    if turtleX > rightBound or turtleX < leftBound:
        exit_x = False
    if turtleY > topBound or turtleY < bottomBound:
        exit_y = False

    return exit_y and exit_x

# in stead of checking the window size, I am setting it so it does not take the automatic 0.5 when I have two screens and becomes HUGE

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

turtlesOnScreen = isOnScreen(window,fiat) and isOnScreen(window, skoda)

while turtlesOnScreen:
    moveTurtle(fiat, 30)
    moveTurtle(skoda, 30)
    turtlesOnScreen = isOnScreen(window,fiat) and isOnScreen(window, skoda)

window.exitonclick()
