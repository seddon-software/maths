from question import Question
from geometry import Point
import drawing
import random
import math


class StraightLine(Question):

    def generate(self):

        self.given = random.choice(
            [30, 40, 50, 60, 70, 80]
        )

        self.answer = 180 - self.given

        self.A = Point(-5, 0)
        self.O = Point(0, 0)
        self.B = Point(5, 0)

        angle = math.radians(self.given)

        length = 4

        self.C = Point(
            length * math.cos(angle),
            length * math.sin(angle)
        )


    def solve(self):
        pass


    def draw(self, ax):

        drawing.line(ax, self.A, self.B)
        drawing.line(ax, self.O, self.C)

        drawing.label(ax, self.A, "A")
        drawing.label(ax, self.O, "O")
        drawing.label(ax, self.B, "B")
        drawing.label(ax, self.C, "C")

        drawing.polar_text(ax, self.O, 0.8, self.given / 2, f"{self.given}°")
        drawing.polar_text(ax, self.O, 0.8, 180 + self.answer / 2, "?", colour="darkorange", size=18)