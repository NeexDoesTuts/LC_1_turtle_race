import turtle
import random

def coinToss():
    return random.randrange(0,2,1)

def moveTurtle(turtle, step):
    direction = coinToss()
    if direction == 0:
        turtle.right(90)
    else:
        turtle.left(90)
    turtle.forward(step)

window = turtle.Screen()

fiat = turtle.Turtle()
skoda = turtle.Turtle()

fiat.color("green")
fiat.speed(10)
skoda.color("blue")
skoda.speed(10)

temp_wall = 0
while temp_wall < 100:
    temp_wall += 1
    moveTurtle(fiat, 10)
    moveTurtle(skoda, 10)

window.exitonclick()
