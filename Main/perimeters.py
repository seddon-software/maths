import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import random
import math


def add_text(ax, x, y, text, rotation=0):
    ax.text(x, y, text,
            ha="center",
            va="center",
            rotation=rotation,
            fontsize=16)


def rectangle_semicircle():
    w = random.randint(8, 14)
    d = random.choice([4, 6, 8])

    radius = d / 2

    fig, ax = plt.subplots(figsize=(7, 5))

    # top line
    ax.plot([w, 0], [d, d], "k")
    # vertical from origin
    ax.plot([0, 0], [0, d], "k")
    # diameter
    ax.plot([w, w], [d, 0], "k--")
    # bottom -> semicircle -> top -> left
    ax.plot([0, w],[0,0], "k")
    ax.add_patch(
        Arc((w, radius),
            d,
            d,
            theta1=-90,
            theta2=90)
    )
    # add_text(ax, w, 0, "w,0")
    # add_text(ax, d, 0, "d,0")
    # add_text(ax, w, d, "w,d")
    # add_text(ax, d, d, "d,d")
    # add_text(ax, 0, 0, "0,0")
    # add_text(ax, 0, d, "0,d")
    add_text(ax, w/2, -0.8,
             f"{w} cm")

    add_text(ax, -0.8, d/2,
             f"{d} cm",
             90)

    perimeter = (
        2 * w +
        d +
        math.pi * radius
    )

    return fig, ax, perimeter


def l_shape():
    m = 0.6
    w = random.randint(12, 18)
    h = random.randint(8, 12)
    w1 = random.randint(2, w//2)
    w2 = random.randint(2, w//2)
    w3 = random.randint(2, w//2)
    w4 = random.randint(2, w//2)
    h1 = random.randint(2, w//5)
    h2 = random.randint(2, w//5)

    points = [
        (0, 0),
        (w1, 0),
        (w1, h1),
        (w-w2, h1),
        (w-w2, 0),
        (w,0),
        (w,h),
        (w-w4,h),
        (w-w4,h-h2),
        (w3,h-h2),
        (w3,h),
        (0, h),
        (0, 0)
    ]

    fig, ax = plt.subplots(figsize=(7, 5))

    xs, ys = zip(*points)
    ax.plot(xs, ys, "k")

    for i,p in enumerate(points):
        if i in [3, 9, 11]: continue
        p1 = points[i]
        try:
            p2 = points[i+1]
        except:
            continue
        p = [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]
        q = [p2[0] - p1[0], p2[1] - p1[1]]
        if q[0] == 0: 
            text = f"{abs(q[1])}cm"
        else:
            text = f"{abs(q[0])}cm"        
        if p1[0] == p2[0]:
            p[0] += m
        else:
            p[1] += m
        add_text(ax, *p, text)
    perimeter = 2 * (w + h + h1 + h2)
    return fig, ax, perimeter


def triangle_roof():
    width = random.randint(8, 14)
    wall_height = random.randint(4, 7)
    sloping_side = random.randint(5, 8)

    points = [
        (0, 0),
        (width, 0),
        (width, wall_height),
        (width/2, wall_height + 3),
        (0, wall_height),
        (0, 0)
    ]

    fig, ax = plt.subplots(figsize=(7, 6))

    xs, ys = zip(*points)
    ax.plot(xs, ys, "k")

    add_text(ax, width/2, -0.8,
             f"{width} cm")

    add_text(ax, -0.8, wall_height/2,
             f"{wall_height} cm",
             90)

    # Both sloping sides are equal
    add_text(ax,
             width/4,
             wall_height+1.5,
             f"{sloping_side} cm")

    add_text(ax,
             3*width/4,
             wall_height+1.5,
             f"{sloping_side} cm")

    perimeter = (
        width +
        2 * wall_height +
        2 * sloping_side
    )

    return fig, ax, perimeter


# -----------------------------
# Generate one question
# -----------------------------

shape = random.choice([
    rectangle_semicircle,
    l_shape,
    triangle_roof
])

fig, ax, answer = shape()

ax.set_aspect("equal")
ax.axis("off")

print()
print("Teacher answer:")
print(f"Perimeter = {answer:.4f} cm")

plt.show()
