import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(a, b):

    return math.hypot(
        a.x - b.x,
        a.y - b.y
    )


def angle(a, b, c):
    """
    angle ABC
    """

    ab = distance(a, b)
    cb = distance(c, b)
    ac = distance(a, c)

    cos_value = (
        ab*ab +
        cb*cb -
        ac*ac
    ) / (2*ab*cb)

    cos_value = max(
        -1,
        min(1, cos_value)
    )

    return math.degrees(
        math.acos(cos_value)
    )

