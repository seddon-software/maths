import math
import random
import tkinter as tk

TITLE = "Isosceles Triangle"
SHOW_TITLE = False
SCREEN_PADDING = 0.10    # fraction of the screen left empty on each side
MIN_SIDE, MAX_SIDE = 5, 25          # side lengths in units
MIN_BASE_ANGLE, MAX_BASE_ANGLE = 30, 75   # keeps the triangle from being too skinny or flat

root = tk.Tk()

# Start at the mouse pointer so fullscreen happens on that monitor
px, py = root.winfo_pointerxy()
root.geometry(f"800x600+{max(px - 400, 0)}+{max(py - 300, 0)}")
root.update()
root.attributes("-fullscreen", True)

# Esc exits
root.bind("<Escape>", lambda e: root.destroy())

canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# State of the current example
ex = {}


def draw_angle(i):
    """Draw a cyan segment and a label at corner i (0 and 1 are the base angles, 2 is the apex)."""
    pts = ex["pts"]
    r = ex["arc_r"]
    vx, vy = pts[i]

    # Unit vectors from this corner to the other two corners
    sum_x = sum_y = 0
    for j in (i - 1, (i + 1) % 3):
        ox, oy = pts[j]
        d = math.hypot(ox - vx, oy - vy)
        sum_x += (ox - vx) / d
        sum_y += (oy - vy) / d

    # Bisector of the angle (screen y points down, so flip it for tk)
    bisector = math.degrees(math.atan2(-sum_y, sum_x))
    extent = ex["angles"][i]

    canvas.create_arc(
        vx - r, vy - r, vx + r, vy + r,
        start=bisector - extent / 2, extent=extent, fill="cyan",
    )

    mid = math.radians(bisector)
    label_r = r * 0.68
    canvas.create_text(
        vx + label_r * math.cos(mid), vy - label_r * math.sin(mid),
        text=f"{extent:.1f}°", font=("Arial", 18),
    )


def new_example():
    """Clear the canvas and draw a fresh isosceles triangle."""
    canvas.delete("all")

    screen_w = canvas.winfo_width()
    screen_h = canvas.winfo_height()
    area_w = screen_w * (1 - 2 * SCREEN_PADDING)
    area_h = screen_h * (1 - 2 * SCREEN_PADDING)

    # Title centred in the empty strip above the drawing area
    if SHOW_TITLE: canvas.create_text(screen_w / 2, screen_h * SCREEN_PADDING / 2,
                       text=TITLE, font=("Arial", 32, "bold"))

    # Re-roll until the triangle is valid, not equilateral, and not too skinny
    while True:
        base = random.randint(MIN_SIDE, MAX_SIDE)
        leg = random.randint(MIN_SIDE, MAX_SIDE)
        if leg <= base / 2 or leg == base:
            continue
        base_angle = math.degrees(math.acos(base / (2 * leg)))
        if MIN_BASE_ANGLE <= base_angle <= MAX_BASE_ANGLE:
            break

    base_angle = round(base_angle, 1)
    apex_angle = round(180 - 2 * base_angle, 1)

    # Build in unit coordinates (y up): base on the x axis, apex above its middle
    h = math.sqrt(leg ** 2 - (base / 2) ** 2)
    units = [(-base / 2, 0), (base / 2, 0), (0, h)]          # A, B, apex C
    gx, gy = 0, h / 3                                        # centroid

    # Rotate randomly around the centroid
    rot = math.radians(random.uniform(0, 360))
    rel = []
    for x, y in units:
        dx, dy = x - gx, y - gy
        rel.append((dx * math.cos(rot) - dy * math.sin(rot),
                    dx * math.sin(rot) + dy * math.cos(rot)))

    # Scale so the triangle fits the drawing area in any orientation
    radius = max(math.hypot(x, y) for x, y in rel)
    longest = max(base, leg)
    scale = (min(area_w, area_h) / 2) / radius * (longest / MAX_SIDE)

    cx, cy = screen_w / 2, screen_h / 2
    pts = [(cx + x * scale, cy - y * scale) for x, y in rel]
    side_px = min(base, leg) * scale

    ex.update(
        pts=pts,
        angles=[base_angle, base_angle, apex_angle],
        arc_r=side_px * 0.3,
        first=random.choice([0, 1]),   # which base angle is shown at the start
        stage=0,                       # 0: one base angle, 1: both base angles, 2: all three
    )

    canvas.create_polygon(
        *[c for p in pts for c in p],
        fill="#90ee90", outline="black", width=3,
    )

    # Edges: base (A-B), then the two legs (B-C, C-A)
    edges = [(0, 1, base, False), (1, 2, leg, True), (2, 0, leg, True)]
    for a, b, length_units, is_leg in edges:
        x1, y1 = pts[a]
        x2, y2 = pts[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy)
        nx, ny = -dy / length, dx / length          # unit normal

        # Make the normal point away from the triangle's centre
        if nx * (mx - cx) + ny * (my - cy) < 0:
            nx, ny = -nx, -ny

        # Tick mark on each of the two equal legs
        if is_leg:
            t = length * 0.03
            canvas.create_line(mx - nx * t, my - ny * t, mx + nx * t, my + ny * t,
                               width=3)

        # Side length, placed outside the triangle
        off = length * 0.05 + 28
        canvas.create_text(mx + nx * off, my + ny * off,
                           text=f"{length_units}", font=("Arial", 22))

    # One of the two equal angles is shown at the start
    draw_angle(ex["first"])


def inside_triangle(x, y):
    """Point-in-triangle test using the sign of the cross product on each edge."""
    signs = []
    for i in range(3):
        x1, y1 = ex["pts"][i]
        x2, y2 = ex["pts"][(i + 1) % 3]
        signs.append((x2 - x1) * (y - y1) - (y2 - y1) * (x - x1))
    return all(s >= 0 for s in signs) or all(s <= 0 for s in signs)


def on_canvas_click(event):
    if inside_triangle(event.x, event.y):
        if ex["stage"] == 0:
            # First click: the other equal angle
            draw_angle(1 - ex["first"])
            ex["stage"] = 1
        elif ex["stage"] == 1:
            # Second click: the remaining (apex) angle
            draw_angle(2)
            ex["stage"] = 2
    else:
        new_example()


canvas.bind("<Button-1>", on_canvas_click)

# Wait briefly for the window manager to finish going fullscreen, then draw
root.after(300, new_example)
root.mainloop()