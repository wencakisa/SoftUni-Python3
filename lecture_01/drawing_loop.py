from turtle import Turtle, done
import sys


def main():
    t = Turtle()
    t.speed('fast')
    t.pensize(10)

    draw_loop(t, 20, 10)
    t.clear()
    draw_olympics_logo(t, 50)
    t.clear()
    draw_telerik_logo(t, 200)

    done()


def draw_loop(turtle: Turtle, side: int, angle: int) -> None:
    colors = ['red', 'green', 'blue', 'purple']
    a = 0

    while True:
        turtle.left(angle % 24)
        turtle.forward(side)
        angle += 1
        a += 1
        turtle.color(colors[a % len(colors)])


def draw_olympics_logo(turtle: Turtle, radius: int) -> None:
    x_coord = -radius * 3
    x_subtract = radius + 20
    colors = ['blue', 'yellow', 'red', 'green', 'black']

    for i in range(0, len(colors), 2):
        turtle.penup()
        turtle.setpos(x_coord, 0)
        turtle.pendown()
        turtle.color(colors[i])
        turtle.circle(radius)

        x_coord += x_subtract

        if i + 1 != len(colors):
            turtle.penup()
            turtle.setpos(x_coord, -radius)
            turtle.pendown()
            turtle.color(colors[i + 1])
            turtle.circle(radius)

            x_coord += x_subtract


def draw_telerik_logo(turtle: Turtle, side: int) -> None:
    turtle.color('green')

    turtle.penup()
    turtle.setpos(-side * 1.5, side)
    turtle.pendown()

    turtle.left(45)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side * 2)
    turtle.right(90)

    for _ in range(2):
        turtle.forward(side)
        turtle.right(90)

    turtle.forward(side * 2)
    turtle.right(90)
    turtle.forward(side)


if __name__ == '__main__':
    sys.exit(main())
