import matplotlib.pyplot as plt
#from matplotlib.patches import Arc
from matplotlib.patches import Wedge
from matplotlib.widgets import Button
import random
import math

pi = 3.14

def add_text(ax, x, y, text, rotation=0):
    ax.text(x, y, text,
            ha="center",
            va="center",
            rotation=rotation,
            fontsize=16)


def shapeA():
    w = random.randint(8, 14)
    d = random.choice([4, 6, 8])

    r = d / 2

    fig, ax = plt.subplots(figsize=(7, 5))
    xs = [0, w, w, 0, 0]
    ys = [0, 0, d, d, 0]

    ax.plot(xs, ys, "k", linewidth=2)
    ax.fill(xs, ys, "lightblue", alpha = 0.3)
    ax.add_patch(
        Wedge(
            center=(w, r),
            r=d/2,
            theta1=-90,
            theta2=90,
            linewidth=2,
            facecolor="lightblue",
            edgecolor="black",
            alpha=0.3
        )
    )
    ax.plot([w, w], [0, d], color="white", linewidth=2)
    ax.plot([w, w], [0, d], "k--", linewidth=2)
    add_text(ax, w/2, -0.8, f"{w} cm")
    add_text(ax, -0.8, d/2, f"{d} cm", 90)

    perimeter = (2*w + d + pi*r)
    area = w*d + pi * r**2/2
    return fig, ax, perimeter, area

def shapeB():
    m = 0.3
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
    ax.fill(xs, ys, color="lightblue", alpha=0.5
    )
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
    area = w*h - (w-w1-w2)*h1 - (w-w3-w4)*h2 
    return fig, ax, perimeter, area


def shapeC():
    w = random.randint(8, 14)
    h = random.randint(4, 7)
    s = random.randint(5, 8)

    points = [
        (0, 0),
        (w, 0),
        (w, h),
        (w/2, h + 3),
        (0, h),
        (0, 0)
    ]

    fig, ax = plt.subplots(figsize=(7, 6))

    xs, ys = zip(*points)
    ax.plot(xs, ys, "k")
    ax.fill(xs, ys, color="lightblue", alpha=0.5)

    add_text(ax, w/2, -0.8, f"{w} cm")
    add_text(ax, -0.8, h/2, f"{h} cm", 90)

    # Both sloping sides are equal
    add_text(ax, w/4, h+1.5, f"{s} cm")
    add_text(ax, 3*w/4, h+1.5, f"{s} cm")

    perimeter = (w + 2*h + 2*s)
    area = w*h + (s**2 - w**2/4)**0.5 / 2
    return fig, ax, perimeter, area


# -----------------------------
# Generate one question
# -----------------------------

shape = random.choice([
    shapeA,
    shapeB,
    shapeC
])

fig, ax, perimeter, area = shape()

ax.set_aspect("equal")
ax.axis("off")

print()
print("Teacher answer:")
print(f"Perimeter = {perimeter:.4f} cm")
print(f"Area = {area:.4f} cm")

plt.show()
