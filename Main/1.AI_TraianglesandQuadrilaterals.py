import math
import random
import tkinter as tk

SCREEN_PADDING = 0.12

MIN_SIDE, MAX_SIDE = 5, 20

root = tk.Tk()
root.title("Quadrilaterals and Triangles")

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
    n = len(pts)
    x, y = pts[i]

    # Bisector of the angle, from the two neighbouring edges.
    prev_pt = pts[(i-1) % n]
    next_pt = pts[(i+1) % n]

    d1 = math.hypot(prev_pt[0]-x, prev_pt[1]-y)
    d2 = math.hypot(next_pt[0]-x, next_pt[1]-y)

    bx = (prev_pt[0]-x)/d1 + (next_pt[0]-x)/d2
    by = (prev_pt[1]-y)/d1 + (next_pt[1]-y)/d2

    # Canvas y points down, Tk arc angles assume y up, so flip y.
    bisector = math.degrees(math.atan2(-by, bx))

    r = ex["arc_r"]
    extent = angles[i]

    # Cyan filled wedge behind the angle value
    canvas.create_arc(
        x-r, y-r, x+r, y+r,
        start=bisector-extent/2,
        extent=extent,
        style="pieslice",
        fill="cyan",
        outline="#0099aa",
        width=2
    )

    label_r = r * 0.7
    mid = math.radians(bisector)

    canvas.create_text(
        x + label_r*math.cos(mid),
        y - label_r*math.sin(mid),
        text=f"{angles[i]:.1f}°",
        font=("Arial", 18, "bold"),
        fill="#cc0000"
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

    # Generate a shape
    shape = random.choice([
        "Square",
        "Rectangle",
        "Rhombus",
        "Parallelogram",
        "Trapezium",
        "Kite",
        "Right-angled triangle",
        "Isosceles triangle",
        "Equilateral triangle"
    ])

    w = random.randint(MIN_SIDE, MAX_SIDE)
    h = random.randint(MIN_SIDE, MAX_SIDE)

    if shape == "Square":
        h = w
        units = [(-w/2,-h/2),(w/2,-h/2),
                 (w/2,h/2),(-w/2,h/2)]

    elif shape == "Rectangle":
        # Avoid w == h so it isn't a square
        while h == w:
            h = random.randint(MIN_SIDE, MAX_SIDE)
        units = [(-w/2,-h/2),(w/2,-h/2),
                 (w/2,h/2),(-w/2,h/2)]

    elif shape == "Rhombus":
        # Side length w, interior angle theta (never 90 degrees)
        theta = math.radians(random.choice(
            [*range(40, 81), *range(100, 141)]
        ))
        dx = w * math.cos(theta/2)
        dy = w * math.sin(theta/2)
        units = [(-dx,0),(0,-dy),
                 (dx,0),(0,dy)]

    elif shape == "Parallelogram":
        # Shear enough that it isn't a rectangle, and the slanted
        # side must differ from w so it isn't a rhombus
        while True:
            offset = random.uniform(-w/3, w/3)
            slant = math.hypot(offset, h)
            if abs(offset) > w*0.1 and abs(slant - w) > 0.5:
                break
        units = [(-w/2,-h/2),(w/2,-h/2),
                 (w/2+offset,h/2),(-w/2+offset,h/2)]

    elif shape == "Trapezium":
        top = random.uniform(w*0.35, w*0.85)
        units = [(-w/2,-h/2),(w/2,-h/2),
                 (top/2,h/2),(-top/2,h/2)]

    elif shape == "Kite":
        # Make top and bottom differ so it isn't a rhombus
        while True:
            top = random.uniform(w*0.3, w*0.7)
            bottom = random.uniform(w*0.3, w*0.7)
            if abs(top - bottom) > w*0.1:
                break
        units = [(0,-h/2),(top/2,0),
                 (0,h/2),(-bottom/2,0)]

    elif shape == "Right-angled triangle":
        # Legs w and h; avoid w == h so it isn't also isosceles
        while h == w:
            h = random.randint(MIN_SIDE, MAX_SIDE)
        units = [(0,0),(w,0),(0,h)]

    elif shape == "Isosceles triangle":
        # Base w, height h; avoid equilateral and right-angled cases
        eq_height = w * math.sqrt(3) / 2
        h = random.uniform(w*0.3, w*1.5)
        while abs(h - eq_height) < w*0.15 or abs(h - w/2) < w*0.1:
            h = random.uniform(w*0.3, w*1.5)
        units = [(-w/2,0),(w/2,0),(0,h)]

    elif shape == "Equilateral triangle":
        height = w * math.sqrt(3) / 2
        units = [(-w/2,0),(w/2,0),(0,height)]

    n = len(units)

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

    for i in range(n):
        a = pts[i]
        b = pts[(i+1)%n]
        sides.append(math.hypot(b[0]-a[0],b[1]-a[1]))

    for i in range(n):
        angles.append(angle_at(
            pts[(i-1)%n], pts[i], pts[(i+1)%n]
        ))

    # Choose the angles shown initially
    if shape == "Kite":
        # Vertices 0 and 2 are the equal pair, 1 and 3 the unequal pair.
        # One of each is always enough to work out the other two.
        first_angles = [random.choice([0, 2]), random.choice([1, 3])]
    else:
        first_angles = [random.randrange(n)]

    ex.update(
        pts=pts,
        angles=angles,
        sides=sides,
        arc_r=min(sides)*0.16,
        stage=1,
        first_angles=first_angles,
        shape=shape
    )

    canvas.create_polygon(
        *[c for p in pts for c in p],
        fill="#90ee90",
        outline="black",
        width=3
    )

    # Side labels
    for i in range(n):
        a = pts[i]
        b = pts[(i+1)%n]

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

    # Show the initial angle(s) immediately
    for i in first_angles:
        draw_angle(i)


def on_canvas_click(event):

    if inside_polygon(event.x, event.y):

        n = len(ex["pts"])
        remaining = [
            i for i in range(n)
            if i not in ex["first_angles"]
        ]

        if ex["stage"] == 1:
            # First click: reveal type only
            canvas.create_text(
                canvas.winfo_width()/2,
                canvas.winfo_height()*0.08,
                text=ex["shape"],
                font=("Arial", 24, "bold")
            )

        elif ex["stage"] <= 1 + len(remaining):
            # Subsequent clicks: reveal one angle
            draw_angle(remaining[ex["stage"]-2])

        ex["stage"] += 1

    else:
        new_example()


canvas.bind("<Button-1>", on_canvas_click)

root.after(300, new_example)
root.mainloop()