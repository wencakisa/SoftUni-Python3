from turtle import *
import sys


def main():
    side = float(input('Enter a side length: '))

    turtle = Turtle()
    turtle.penup()
    turtle.setx(-side / 2)
    turtle.sety(side / 2)
    turtle.pendown()
    turtle.speed('slowest')
    turtle.color('green')

    for i in range(4):
        turtle.forward(side)
        turtle.right(90)


if __name__ == '__main__':
    sys.exit(main())
