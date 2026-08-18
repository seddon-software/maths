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
    a = math.dist(p2, p3)
    b = math.dist(p1, p3)
    c = math.dist(p1, p2)

    cos = (a*a + c*c - b*b)/(2*a*c)
    cos = max(-1, min(1, cos))

    return math.degrees(math.acos(cos))


def draw_right_angle(ax, vertex, p1, p2, size=0.35):

    v = np.array(vertex)

    a = np.array(p1)-v
    b = np.array(p2)-v

    a = a/np.linalg.norm(a)*size
    b = b/np.linalg.norm(b)*size

    pA=v+a
    pB=pA+b
    pC=v+b

    ax.plot(
        [pA[0],pB[0],pC[0]],
        [pA[1],pB[1],pC[1]],
        "k",
        linewidth=2
    )


def draw_tick(ax,p1,p2):

    p1=np.array(p1)
    p2=np.array(p2)

    mid=(p1+p2)/2

    d=p2-p1
    d=d/np.linalg.norm(d)

    n=np.array([-d[1],d[0]])

    a=mid-n*0.22
    b=mid+n*0.22

    ax.plot([a[0],b[0]],[a[1],b[1]],"k",linewidth=2)


def draw_angle_arc(ax, point, p1, p2, radius, colour):

    p=np.array(point)
    a=np.array(p1)-p
    b=np.array(p2)-p

    ang1=math.degrees(math.atan2(a[1],a[0]))
    ang2=math.degrees(math.atan2(b[1],b[0]))

    if ang2<ang1:
        ang1,ang2=ang2,ang1

    arc=patches.Arc(
        point,
        radius*2,
        radius*2,
        theta1=ang1,
        theta2=ang2,
        color=colour,
        linewidth=2
    )

    ax.add_patch(arc)


# ----------------------------------------------------
# Random geometry
# ----------------------------------------------------

base=random.randint(5,9)
height=random.randint(3,7)

A=(0,0)
B=(base,0)
C=(base,height)

D=(base+random.randint(4,7),0)

# Apex angle chosen first
apex=random.choice([30,40,50,60,70,80])

mid=(B[0]+D[0])/2
half=(D[0]-B[0])/2

h=half/math.tan(math.radians(apex/2))

E=(mid,h)

# ----------------------------------------------------
# Answers
# ----------------------------------------------------

angle_A=angle_between(B,A,C)
angle_D=(180-apex)/2

missing=random.choice(["A","D"])
answer=angle_A if missing=="A" else angle_D

# ----------------------------------------------------
# Draw
# ----------------------------------------------------

fig,ax=plt.subplots(figsize=(9,6))

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

draw_right_angle(ax,B,A,C)

draw_tick(ax,B,E)
draw_tick(ax,E,D)

# arcs
draw_angle_arc(ax,A,B,C,0.8,
               "darkorange" if missing=="A" else "blue")

draw_angle_arc(ax,D,B,E,0.8,
               "darkorange" if missing=="D" else "blue")

draw_angle_arc(ax,E,B,D,0.6,"blue")

# labels
for name,p in [("A",A),("B",B),("C",C),("D",D),("E",E)]:
    add_text(ax,p[0],p[1]+0.35,name,
             colour="red",weight="bold")

# A
if missing=="A":
    add_text(ax,A[0]+0.7,A[1]+0.5,"?",
             size=18,colour="darkorange",weight="bold")
else:
    add_text(ax,A[0]+0.7,A[1]+0.5,
             f"{angle_A:.0f}°",
             colour="blue")

# D
if missing=="D":
    add_text(ax,D[0]-0.5,D[1]+0.5,"?",
             size=18,colour="darkorange",weight="bold")
else:
    add_text(ax,D[0]-0.5,D[1]+0.5,
             f"{angle_D:.0f}°",
             colour="blue")

# Apex angle (always shown)
add_text(ax,E[0],E[1]-0.55,f"{apex}°",colour="blue")

ax.set_aspect("equal")
ax.axis("off")

plt.title(f"Find the missing angle {missing}",
          fontsize=16,
          weight="bold")

print(f"Answer = {answer:.1f}°")

plt.show()