from turtle import Turtle, done
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
    turtle.pensize(5)

    for i in range(4):
        turtle.forward(side)
        turtle.right(90)

    done()

if __name__ == '__main__':
    sys.exit(main())
