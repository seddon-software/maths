import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import math
import numpy as np


def add_text(ax, x, y, text, size=12, colour="black", weight="normal"):
    ax.text(
        x, y, text,
        fontsize=size,
        color=colour,
        fontweight=weight,
        ha="center",
        va="center"
    )


def angle_between(p1, p2, p3):
    """Angle at p2"""

    a = math.dist(p2, p3)
    b = math.dist(p1, p3)
    c = math.dist(p1, p2)

    cos_angle = (a*a + c*c - b*b)/(2*a*c)
    cos_angle = max(-1, min(1, cos_angle))

    return math.degrees(math.acos(cos_angle))


def draw_right_angle(ax, vertex, p1, p2, size=0.35):

    v = np.array(vertex)

    a = np.array(p1)-v
    b = np.array(p2)-v

    a = a/np.linalg.norm(a)*size
    b = b/np.linalg.norm(b)*size

    pA = v+a
    pB = pA+b
    pC = v+b

    ax.plot(
        [pA[0], pB[0], pC[0]],
        [pA[1], pB[1], pC[1]],
        color="black",
        linewidth=2
    )


def draw_tick(ax, p1, p2):

    p1=np.array(p1)
    p2=np.array(p2)

    mid=(p1+p2)/2

    d=p2-p1
    d=d/np.linalg.norm(d)

    n=np.array([-d[1], d[0]])

    a=mid-n*0.25
    b=mid+n*0.25

    ax.plot(
        [a[0],b[0]],
        [a[1],b[1]],
        "k",
        linewidth=2
    )


def draw_angle_arc(ax, point, p1, p2, radius,
                   colour="blue"):

    """
    Draw an arc at point between p1 and p2
    """

    p=np.array(point)
    a=np.array(p1)-p
    b=np.array(p2)-p

    angle1=math.degrees(math.atan2(a[1],a[0]))
    angle2=math.degrees(math.atan2(b[1],b[0]))

    if angle2 < angle1:
        angle1, angle2 = angle2, angle1

    arc = patches.Arc(
        point,
        radius*2,
        radius*2,
        angle=0,
        theta1=angle1,
        theta2=angle2,
        color=colour,
        linewidth=2
    )

    ax.add_patch(arc)


# -----------------------------------
# Generate geometry
# -----------------------------------

base=random.randint(5,9)
height=random.randint(3,7)


# Right triangle

A=(0,0)
B=(base,0)
C=(base,height)


# Isosceles triangle

D=(base+random.randint(3,6),0)

E=(
    (B[0]+D[0])/2,
    random.randint(3,7)
)


# -----------------------------------
# Angles
# -----------------------------------

angle_A=angle_between(B,A,C)

angle_D=(180-angle_between(B,E,D))/2


# -----------------------------------
# Choose missing angle
# -----------------------------------

missing=random.choice(["A","D"])

answer=angle_A if missing=="A" else angle_D


# -----------------------------------
# Drawing
# -----------------------------------

fig,ax=plt.subplots(figsize=(9,6))


# Filled shapes

ax.add_patch(
    patches.Polygon(
        [A,B,C],
        closed=True,
        facecolor="#d8ecff",
        edgecolor="black",
        linewidth=2
    )
)


ax.add_patch(
    patches.Polygon(
        [B,D,E],
        closed=True,
        facecolor="#ddf5dd",
        edgecolor="black",
        linewidth=2
    )
)


# Right angle

draw_right_angle(ax,B,A,C)


# Equal sides

draw_tick(ax,B,E)
draw_tick(ax,E,D)


# -----------------------------------
# Angle arcs
# -----------------------------------

if missing=="A":

    draw_angle_arc(
        ax,A,B,C,
        0.8,
        "darkorange"
    )

else:

    draw_angle_arc(
        ax,A,B,C,
        0.8,
        "blue"
    )


if missing=="D":

    draw_angle_arc(
        ax,D,B,E,
        0.8,
        "darkorange"
    )

else:

    draw_angle_arc(
        ax,D,B,E,
        0.8,
        "blue"
    )


# -----------------------------------
# Vertex labels
# -----------------------------------

for name,p in [
    ("A",A),
    ("B",B),
    ("C",C),
    ("D",D),
    ("E",E)
]:

    add_text(
        ax,
        p[0],
        p[1]+0.35,
        name,
        colour="red",
        weight="bold"
    )


# -----------------------------------
# Angle values
# -----------------------------------

if missing!="A":

    add_text(
        ax,
        A[0]+0.7,
        A[1]+0.55,
        f"{angle_A:.0f}°",
        colour="blue"
    )


else:

    add_text(
        ax,
        A[0]+0.7,
        A[1]+0.55,
        "?",
        size=18,
        colour="darkorange",
        weight="bold"
    )


if missing!="D":

    add_text(
        ax,
        D[0]-0.5,
        D[1]+0.55,
        f"{angle_D:.0f}°",
        colour="blue"
    )


else:

    add_text(
        ax,
        D[0]-0.5,
        D[1]+0.55,
        "?",
        size=18,
        colour="darkorange",
        weight="bold"
    )


# -----------------------------------
# Title and display
# -----------------------------------

ax.set_aspect("equal")
ax.axis("off")

plt.title(
    f"Find the missing angle {missing}\n",
    fontsize=16,
    weight="bold"
)

plt.show()


print("-----------------------")
print(f"Answer = {answer:.1f} degrees")
