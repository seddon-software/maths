import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import math


def add_text(ax, x, y, text, size=12, colour="black", weight="normal"):
    ax.text(
        x, y, text,
        fontsize=size,
        color=colour,
        fontweight=weight,
        ha="center",
        va="center"
    )


def draw_tick(ax, p1, p2):
    """Draw equal-side tick mark"""

    x1, y1 = p1
    x2, y2 = p2

    mx = (x1+x2)/2
    my = (y1+y2)/2

    dx = x2-x1
    dy = y2-y1

    length = math.sqrt(dx*dx+dy*dy)

    nx = -dy/length
    ny = dx/length

    size = 0.15

    ax.plot(
        [mx-nx*size, mx+nx*size],
        [my-ny*size, my+ny*size],
        "k",
        linewidth=2
    )


def draw_angle_arc(ax, centre, start, end, radius=0.5, colour="blue"):

    cx, cy = centre

    a1 = math.degrees(
        math.atan2(start[1]-cy, start[0]-cx)
    )

    a2 = math.degrees(
        math.atan2(end[1]-cy, end[0]-cx)
    )

    if a2 < a1:
        a1, a2 = a2, a1

    arc = patches.Arc(
        centre,
        radius*2,
        radius*2,
        theta1=a1,
        theta2=a2,
        color=colour,
        linewidth=2
    )

    ax.add_patch(arc)


# --------------------------------------
# Create question
# --------------------------------------

# Apex angle shown at C

apex = random.choice(
    [30, 40, 50, 60, 70, 80]
)

answer = (180 - apex) / 2


# Decide which base angle is missing

missing = random.choice(["A", "B"])


# --------------------------------------
# Fixed geometry
# --------------------------------------

A = (0, 0)
B = (10, 0)
C = (5, 5)


# --------------------------------------
# Draw
# --------------------------------------

fig, ax = plt.subplots(figsize=(7, 5))


triangle = patches.Polygon(
    [A, B, C],
    closed=True,
    facecolor="#ddf5dd",
    edgecolor="black",
    linewidth=2
)

ax.add_patch(triangle)


# Equal sides AC and BC

draw_tick(ax, A, C)
draw_tick(ax, B, C)


# Angle arcs

draw_angle_arc(
    ax,
    C,
    A,
    B
)

draw_angle_arc(
    ax,
    A,
    B,
    C
)

draw_angle_arc(
    ax,
    B,
    A,
    C
)


# Labels

for name, point in [
    ("A", A),
    ("B", B),
    ("C", C)
]:
    add_text(
        ax,
        point[0],
        point[1]-0.5 if name!="C" else point[1]+0.5,
        name,
        colour="red",
        weight="bold"
    )


# Given angle

add_text(
    ax,
    5,
    4.1,
    f"{apex}°",
    colour="blue"
)


# Missing angle

if missing == "A":

    add_text(
        ax,
        1,
        0.8,
        "?",
        size=18,
        colour="darkorange",
        weight="bold"
    )

else:

    add_text(
        ax,
        9,
        0.8,
        "?",
        size=18,
        colour="darkorange",
        weight="bold"
    )


ax.set_aspect("equal")
ax.axis("off")

plt.title(
    "Find the missing angle",
    fontsize=16,
    weight="bold"
)


print("-----------------------")
print(f"Missing angle {missing}")
print(f"Answer = {answer:.0f}°")


plt.show()
