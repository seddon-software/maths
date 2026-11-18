import math
import random
import tkinter as tk

SCREEN_PADDING = 0.10    # fraction of the screen left empty on each side
MIN_SIDE, MAX_SIDE = 8, 25   # side length in units (sets the triangle size)

root = tk.Tk()
SHOW_TITLE = False
TITLE = "Equilateral Triangle"

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


def draw_angles():
    """Draw a cyan segment and a 60° label at each corner."""
    pts = ex["pts"]
    r = ex["arc_r"]
    cx, cy = ex["cx"], ex["cy"]

    for vx, vy in pts:
        # Direction from this corner towards the triangle centre
        # (screen y points down, so flip it for tk's counter-clockwise angles)
        bisector = math.degrees(math.atan2(-(cy - vy), cx - vx))

        canvas.create_arc(
            vx - r, vy - r, vx + r, vy + r,
            start=bisector - 30, extent=60, fill="cyan",
        )

        mid = math.radians(bisector)
        label_r = r * 0.7
        canvas.create_text(
            vx + label_r * math.cos(mid), vy - label_r * math.sin(mid),
            text="60°", font=("Arial", 20),
        )


def new_example():
    """Clear the canvas and draw a fresh equilateral triangle."""
    canvas.delete("all")

    screen_w = canvas.winfo_width()
    screen_h = canvas.winfo_height()

    area_w = screen_w * (1 - 2 * SCREEN_PADDING)
    area_h = screen_h * (1 - 2 * SCREEN_PADDING)

    # Largest side that fits the drawing area in any orientation
    # (circumradius = side / sqrt(3), so the triangle fits in a circle of that radius)
    max_px = min(area_w, area_h) * math.sqrt(3) / 2
    side_units = random.randint(MIN_SIDE, MAX_SIDE)
    side = side_units / MAX_SIDE * max_px

    circ_r = side / math.sqrt(3)
    cx, cy = screen_w / 2, screen_h / 2
    rotation = random.uniform(0, 120)   # degrees; 120° is a full cycle of symmetry

    pts = []
    for i in range(3):
        a = math.radians(rotation + 90 + i * 120)
        pts.append((cx + circ_r * math.cos(a), cy - circ_r * math.sin(a)))

    ex.update(
        pts=pts, cx=cx, cy=cy, side=side,
        arc_r=side * 0.22,
    )

    canvas.create_polygon(
        *[c for p in pts for c in p],
        fill="#90ee90", outline="black", width=3,
    )

    for i in range(3):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % 3]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy)
        nx, ny = -dy / length, dx / length   # unit normal

        # Tick mark to show the sides are equal
        t = side * 0.03
        canvas.create_line(mx - nx * t, my - ny * t, mx + nx * t, my + ny * t,
                           width=3)

        # Side length, placed outside the triangle (away from the centre)
        ox, oy = mx - cx, my - cy
        olen = math.hypot(ox, oy)
        off = side * 0.05 + 28
        canvas.create_text(mx + ox / olen * off, my + oy / olen * off,
                           text=f"{side_units}", font=("Arial", 22))

    # Title just above everything drawn so far (triangle, ticks, side labels)
    left, top, right, bottom = canvas.bbox("all")
    if SHOW_TITLE: canvas.create_text(cx, top - 15, text=TITLE,
                       font=("Arial", 32, "bold"), anchor="s")


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
        if not ex["revealed"]:
            ex["revealed"] = True
            draw_angles()
    else:
        new_example()
        ex["revealed"] = False


canvas.bind("<Button-1>", on_canvas_click)

# Wait briefly for the window manager to finish going fullscreen, then draw
def first_example():
    new_example()
    ex["revealed"] = False

root.after(300, first_example)
root.mainloop()