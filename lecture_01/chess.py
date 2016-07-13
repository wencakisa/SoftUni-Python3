from turtle import Turtle, done
import sys


def main():
    dimension = int(input('Enter dimension: '))

    t = Turtle()
    t.speed('fastest')
    t.pensize(3)

    draw_table(dimension, 50, t, -200, 300)


def draw_table(dimension: int, side: int, turtle: Turtle, x_coord: int, y_coord: int) -> None:
    fill = False

    for i in range(dimension ** 2):
        if i % dimension == 0:
            y_coord -= side
            turtle.penup()
            turtle.setpos(x_coord, y_coord)
            turtle.pendown()
            fill = fill != (dimension % 2 == 0)

        if fill:
            turtle.begin_fill()

        for _ in range(4):
            turtle.forward(side)
            turtle.right(90)

        if turtle.filling():
            turtle.end_fill()

        turtle.forward(side)

        fill = not fill

    done()


if __name__ == '__main__':
    sys.exit(main())
