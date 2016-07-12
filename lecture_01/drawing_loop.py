from turtle import *
import sys

MAGIC_NUM = 1.23


def main():
    angle = float(input('Enter an angle: '))
    length = float(input('Enter a side length: '))
    iterations = int(input('Enter iterations count: '))

    turtle = Turtle()
    turtle.penup()
    turtle.setx(length / 2)
    turtle.sety(-length / 2)
    turtle.pendown()
    turtle.speed('fast')
    turtle.color('green')

    for i in range(iterations):
        turtle.left(angle)
        turtle.forward(length)
        turtle.right(angle)
        angle *= MAGIC_NUM


if __name__ == '__main__':
    sys.exit(main())
