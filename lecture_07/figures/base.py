from turtle import Turtle


class Figure:
    def __init__(self, center_x: int=0, center_y: int=0, color: str='black', **_):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

        if any(v is None for v in self.__dict__.values()):
            raise ValueError('Arguments missing.')

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, str(self.__dict__))

    def draw(self, t: Turtle):
        t.speed('fastest')
        t.color(self.color)
        t.pensize(2)
        self.jump_to(t, 0, 0)

    @staticmethod
    def jump_to(t: Turtle, x: int, y: int):
        t.penup()
        t.setpos(x, y)
        t.pendown()
