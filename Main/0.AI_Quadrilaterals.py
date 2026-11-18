
import math
import random
import tkinter as tk

SCREEN_PADDING = 0.12

MIN_SIDE, MAX_SIDE = 5, 20

root = tk.Tk()
root.title("Quadrilaterals")

px, py = root.winfo_pointerxy()
root.geometry(f"800x600+{max(px - 400, 0)}+{max(py - 300, 0)}")
root.update()
root.attributes("-fullscreen", True)

root.bind("<Escape>", lambda e: root.destroy())

canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)

ex = {}


def angle_at(a, b, c):
    """Interior angle at vertex b, in degrees."""
    v1 = (a[0] - b[0], a[1] - b[1])
    v2 = (c[0] - b[0], c[1] - b[1])

    dot = v1[0]*v2[0] + v1[1]*v2[1]
    d1 = math.hypot(*v1)
    d2 = math.hypot(*v2)

    cosine = max(-1, min(1, dot / (d1*d2)))
    return math.degrees(math.acos(cosine))


def rotate(points, angle):
    """Rotate points around their centroid."""
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)

    result = []
    for x, y in points:
        dx, dy = x-cx, y-cy
        result.append((
            dx*math.cos(angle) - dy*math.sin(angle),
            dx*math.sin(angle) + dy*math.cos(angle)
        ))
    return result


def draw_angle(i):
    pts = ex["pts"]
    angles = ex["angles"]
    x, y = pts[i]

    # Find the interior direction using the polygon centroid.
    centre_x = sum(p[0] for p in pts) / 4
    centre_y = sum(p[1] for p in pts) / 4

    mid_x = centre_x - x
    mid_y = y - centre_y
    bisector = math.degrees(math.atan2(mid_y, mid_x))

    r = ex["arc_r"]
    extent = angles[i]

    canvas.create_arc(
        x-r, y-r, x+r, y+r,
        start=bisector-extent/2,
        extent=extent,
        style="arc",
        outline="cyan",
        width=3
    )

    label_r = r * 0.75
    mid = math.radians(bisector)

    canvas.create_text(
        x + label_r*math.cos(mid),
        y - label_r*math.sin(mid),
        text=f"{angles[i]:.1f}°",
        font=("Arial", 18)
    )


def inside_polygon(x, y):
    """Ray casting point-in-polygon test."""
    pts = ex["pts"]
    inside = False
    j = len(pts)-1

    for i in range(len(pts)):
        xi, yi = pts[i]
        xj, yj = pts[j]

        if ((yi > y) != (yj > y)):
            cross = (xj-xi)*(y-yi)/(yj-yi) + xi
            if x < cross:
                inside = not inside

        j = i

    return inside


def new_example():
    canvas.delete("all")

    screen_w = canvas.winfo_width()
    screen_h = canvas.winfo_height()

    area_w = screen_w * (1-2*SCREEN_PADDING)
    area_h = screen_h * (1-2*SCREEN_PADDING)

    # Generate a quadrilateral
    shape = random.choice([
        "Square",
        "Rectangle",
        "Rhombus",
        "Parallelogram",
        "Trapezium",
        "Kite"
    ])

    w = random.randint(MIN_SIDE, MAX_SIDE)
    h = random.randint(MIN_SIDE, MAX_SIDE)

    if shape == "Square":
        h = w
        units = [(-w/2,-h/2),(w/2,-h/2),
                 (w/2,h/2),(-w/2,h/2)]

    elif shape == "Rectangle":
        units = [(-w/2,-h/2),(w/2,-h/2),
                 (w/2,h/2),(-w/2,h/2)]

    elif shape == "Rhombus":
        angle = math.radians(random.randint(45, 135))
        dx = w * math.cos(angle)
        dy = w * math.sin(angle)
        units = [(-dx/2,0),(0,-dy/2),
                 (dx/2,0),(0,dy/2)]

    elif shape == "Parallelogram":
        offset = random.uniform(-w/3, w/3)
        units = [(-w/2,-h/2),(w/2,-h/2),
                 (w/2+offset,h/2),(-w/2+offset,h/2)]

    elif shape == "Trapezium":
        top = random.uniform(w*0.35, w*0.85)
        units = [(-w/2,-h/2),(w/2,-h/2),
                 (top/2,h/2),(-top/2,h/2)]

    elif shape == "Kite":
        top = random.uniform(w*0.3, w*0.7)
        bottom = random.uniform(w*0.3, w*0.7)
        units = [(0,-h/2),(top/2,0),
                 (0,h/2),(-bottom/2,0)]

    # Rotate
    units = rotate(units, math.radians(random.uniform(0,360)))

    # Scale to fit screen
    radius = max(math.hypot(x,y) for x,y in units)
    scale = min(area_w,area_h)*0.42/radius

    cx, cy = screen_w/2, screen_h/2

    pts = [(cx+x*scale, cy-y*scale) for x,y in units]

    # Calculate side lengths and angles
    sides = []
    angles = []

    for i in range(4):
        a = pts[i]
        b = pts[(i+1)%4]
        sides.append(math.hypot(b[0]-a[0],b[1]-a[1]))

    for i in range(4):
        angles.append(angle_at(
            pts[(i-1)%4], pts[i], pts[(i+1)%4]
        ))

    # Randomly choose the angle shown initially
    first_angle = random.randrange(4)

    ex.update(
        pts=pts,
        angles=angles,
        sides=sides,
        arc_r=min(sides)*0.16,
        stage=1,
        first_angle=first_angle,
        shape=shape
    )

    canvas.create_polygon(
        *[c for p in pts for c in p],
        fill="#90ee90",
        outline="black",
        width=3
    )

    # Side labels
    for i in range(4):
        a = pts[i]
        b = pts[(i+1)%4]

        mx, my = (a[0]+b[0])/2, (a[1]+b[1])/2

        dx, dy = b[0]-a[0], b[1]-a[1]
        length = math.hypot(dx,dy)

        nx, ny = -dy/length, dx/length

        # Point away from centre
        if nx*(mx-cx)+ny*(my-cy) < 0:
            nx,ny = -nx,-ny

        canvas.create_text(
            mx+nx*30,
            my+ny*30,
            text=f"{sides[i]/scale:.1f}",
            font=("Arial",18)
        )

    # Show the first angle immediately
    draw_angle(first_angle)


def on_canvas_click(event):

    if inside_polygon(event.x, event.y):

        if ex["stage"] == 1:
            # First click: reveal type only
            canvas.create_text(
                canvas.winfo_width()/2,
                canvas.winfo_height()*0.08,
                text=ex["shape"],
                font=("Arial", 24, "bold")
            )

        elif ex["stage"] <= 4:
            # Subsequent clicks: reveal one angle
            remaining = [
                i for i in range(4)
                if i != ex["first_angle"]
            ]

            draw_angle(remaining[ex["stage"]-2])

        ex["stage"] += 1

    else:
        new_example()


canvas.bind("<Button-1>", on_canvas_click)

root.after(300, new_example)
root.mainloop()
