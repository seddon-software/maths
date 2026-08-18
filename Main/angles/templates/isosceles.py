import random

from question import Question
from geometry import Point
import drawing


class IsoscelesTriangle(Question):

    def generate(self):

        # angle at the top of the triangle
        self.apex = random.choice(
            [30, 40, 50, 60, 70]
        )

        # choose which base angle is hidden
        self.missing = random.choice(
            ["A", "B"]
        )

        self.answer = (180 - self.apex) / 2


        # fixed layout
        self.A = Point(0, 0)
        self.B = Point(10, 0)
        self.C = Point(5, 5)


    def solve(self):
        # already calculated in generate()
        pass


    def draw(self, ax):

        drawing.polygon(
            ax,
            [
                self.A,
                self.B,
                self.C
            ]
        )


        # equal-side marks
        drawing.tick(
            ax,
            self.A,
            self.C
        )

        drawing.tick(
            ax,
            self.B,
            self.C
        )


        # labels
        drawing.label(ax, self.A, "A")
        drawing.label(ax, self.B, "B")
        drawing.label(ax, self.C, "C")


        drawing.text(
            ax,
            5,
            4.2,
            f"{self.apex}°"
        )

        # missing angle
        if self.missing == "A":

            ax.text(
                1,
                0.8,
                "?",
                fontsize=18,
                color="darkorange",
                fontweight="bold"
            )

        else:

            ax.text(
                9,
                0.8,
                "?",
                fontsize=18,
                color="darkorange",
                fontweight="bold"
            )

