import matplotlib.patches as patches
import numpy as np

import math


def polar_text(ax, point, distance, angle, value,
               colour="blue", size=12):

    x = point.x + distance * math.cos(math.radians(angle))
    y = point.y + distance * math.sin(math.radians(angle))

    text(ax, x, y, value, colour, size)
        
def label(ax, point, text, colour="red"):

    ax.text(
        point.x,
        point.y,
        text,
        color=colour,
        fontsize=14,
        fontweight="bold",
        ha="center",
        va="center"
    )


def text(ax, x, y, value, colour="blue", size=12):

    ax.text(
        x,
        y,
        value,
        fontsize=size,
        color=colour,
        ha="center",
        va="center"
    )


def line(ax, a, b):

    ax.plot(
        [a.x, b.x],
        [a.y, b.y],
        "k"
    )


def polygon(ax, points):

    ax.add_patch(
        patches.Polygon(
            [(p.x, p.y) for p in points],
            closed=True,
            facecolor="#ddf5dd",
            edgecolor="black"
        )
    )


def tick(ax, a, b):
    """
    Draw an equal-length tick mark on a line
    """

    mx = (a.x + b.x) / 2
    my = (a.y + b.y) / 2

    dx = b.x - a.x
    dy = b.y - a.y

    length = np.hypot(dx, dy)

    nx = -dy / length
    ny = dx / length

    size = 0.2

    ax.plot(
        [mx - nx * size, mx + nx * size],
        [my - ny * size, my + ny * size],
        "k",
        linewidth=2
    )


def angle_arc(ax, centre, radius, start_angle, end_angle, colour="blue"):

    ax.add_patch(
        patches.Arc(
            (centre.x, centre.y),
            radius * 2,
            radius * 2,
            theta1=start_angle,
            theta2=end_angle,
            color=colour,
            linewidth=2
        )
    )
