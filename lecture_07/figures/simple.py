from .base import Figure, Turtle


class Circle(Figure):
    def __init__(self, radius: int, **kwargs):
        super().__init__(**kwargs)

        self.radius = radius
        self.steps = None

    def draw(self, turtle_instance: Turtle):
        super().draw(turtle_instance)

        self.jump_to(turtle_instance, x=self.center_x, y=self.center_y - self.radius)
        turtle_instance.circle(radius=self.radius, steps=self.steps)


class Rectangle(Figure):
    def __init__(self, width: int, height: int, **kwargs):
        super().__init__(**kwargs)

        self.width = width
        self.height = height

    def draw(self, turtle_instance: Turtle):
        super().draw(turtle_instance)

        self.jump_to(turtle_instance, self.center_x - self.width / 2, self.center_y + self.height / 2)

        for _ in range(2):
            turtle_instance.forward(self.width)
            turtle_instance.right(90)
            turtle_instance.forward(self.height)
            turtle_instance.right(90)


class Square(Rectangle):
    def __init__(self, side: int, **kwargs):
        super().__init__(width=side, height=side, **kwargs)
