from .base import Figure, Turtle


class Circle(Figure):
    def __init__(self, radius: int, **kwargs):
        super().__init__(**kwargs)

        self.radius = radius
        self.steps = None

    def draw(self, t: Turtle):
        super().draw(t)

        self.jump_to(t, x=self.center_x, y=self.center_y - self.radius)
        t.circle(radius=self.radius, steps=self.steps)


class Rectangle(Figure):
    def __init__(self, width: int, height: int, **kwargs):
        super().__init__(**kwargs)

        self.width = width
        self.height = height

    def draw(self, t: Turtle):
        super().draw(t)

        self.jump_to(t, self.center_x - self.width / 2, self.center_y + self.height / 2)

        for _ in range(2):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)


class Square(Rectangle):
    def __init__(self, side: int, **kwargs):
        super().__init__(width=side, height=side, **kwargs)
