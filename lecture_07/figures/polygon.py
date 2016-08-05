from .simple import Circle


class Polygon(Circle):
    def __init__(self, radius: int, sides: int, **kwargs):
        super().__init__(radius=radius, **kwargs)

        self.steps = sides


class Triangle(Polygon):
    def __init__(self, area: int, **kwargs):
        super().__init__(radius=area, sides=3, **kwargs)
