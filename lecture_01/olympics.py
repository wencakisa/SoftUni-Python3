from turtle import *
import sys

radius = 120
x_subtract = radius + 20
colors = ['blue', 'yellow', 'red', 'green', 'black']


def main():
    turtle = Turtle()
    turtle.pensize(5)
    x = -300

    for i in range(0, len(colors), 2):
        turtle.penup()
        turtle.setx(x)
        turtle.sety(0)
        turtle.pendown()
        turtle.color(colors[i])
        turtle.circle(radius)

        x += x_subtract

        if i + 1 != len(colors):
            turtle.penup()
            turtle.setx(x)
            turtle.sety(-100)
            turtle.pendown()
            turtle.color(colors[i + 1])
            turtle.circle(radius)

            x += x_subtract


if __name__ == '__main__':
    sys.exit(main())
