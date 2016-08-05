from turtle import Turtle


class Figure:
    def __init__(self, center_x: int=0, center_y: int=0, color: str='black', **kwargs):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

        if any(v is None for v in self.__dict__.values()):
            raise ValueError('Arguments missing.')

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, str(self.__dict__))

    def draw(self, turtle_instance: Turtle):
        turtle_instance.speed(speed='fast')
        turtle_instance.color(self.color)
        turtle_instance.pensize(2)
        self.jump_to(turtle_instance, 0, 0)

    @staticmethod
    def jump_to(turtle_instance: Turtle, x: int, y: int):
        turtle_instance.penup()
        turtle_instance.setpos(x, y)
        turtle_instance.pendown()
