import math
import random
import tkinter as tk

SCREEN_PADDING = 0.10    # fraction of the screen left empty on each side
MIN_SIDE, MAX_SIDE = 5, 25
MIN_ANGLE, MAX_ANGLE = 25, 65

root = tk.Tk()
root.title("Right Angle Triangle")

# Full screen: Esc exits, F11 toggles
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.destroy())
root.bind("<F11>", lambda e: root.attributes(
    "-fullscreen", not root.attributes("-fullscreen")))

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

canvas = tk.Canvas(root, width=screen_w, height=screen_h, bg="white",
                   highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Drawing area: the middle 80% of the screen
area_w = screen_w * (1 - 2 * SCREEN_PADDING)
area_h = screen_h * (1 - 2 * SCREEN_PADDING)
area_left = screen_w * SCREEN_PADDING
area_top = screen_h * SCREEN_PADDING

# One scale for both sides (pixels per unit), so a side of MAX_SIDE just fits
scale = min(area_w, area_h) / MAX_SIDE

# State of the current example
ex = {}


def draw_angle(bottom_corner):
    """Draw a filled cyan segment and its label at the bottom-right or the top corner."""
    if bottom_corner:
        vx, vy = ex["x1"], ex["y1"]
        start, extent = 180 - ex["angle_bottom"], ex["angle_bottom"]   # tk angles: counter-clockwise from east
        shown = ex["angle_bottom"]
    else:
        vx, vy = ex["x2"], ex["y2"]
        start, extent = 270, ex["angle_top"]
        shown = ex["angle_top"]

    r = ex["arc_r"]

    # Filled pie-slice segment
    canvas.create_arc(
        vx - r, vy - r, vx + r, vy + r,
        start=start, extent=extent, fill="cyan",
    )

    # Label inside the segment, along the bisector of the angle
    mid = math.radians(start + extent / 2)
    label_r = r * 0.7
    canvas.create_text(
        vx + label_r * math.cos(mid), vy - label_r * math.sin(mid),
        text=f"{shown:.1f}°", font=("Arial", 24),
    )


def new_example():
    """Clear the canvas, pick new sides and draw a fresh triangle."""
    canvas.delete("all")

    # Re-roll until both acute angles are between MIN_ANGLE and MAX_ANGLE
    while True:
        adjacent = random.randint(MIN_SIDE, MAX_SIDE)   # horizontal side
        opposite = random.randint(MIN_SIDE, MAX_SIDE)   # vertical side
        angle_bottom = math.degrees(math.atan2(opposite, adjacent))   # bottom-right corner
        angle_top = 90 - angle_bottom                                  # top corner
        if MIN_ANGLE <= angle_bottom <= MAX_ANGLE:   # angle_top is then in range too
            break

    tri_w = adjacent * scale
    tri_h = opposite * scale

    # Centre the triangle inside the drawing area
    left = area_left + (area_w - tri_w) / 2
    right = left + tri_w
    bottom = area_top + (area_h + tri_h) / 2
    top = bottom - tri_h

    # Corners: the right angle is at the bottom-left
    x0, y0 = left, bottom      # right-angle corner
    x1, y1 = right, bottom     # end of the adjacent side
    x2, y2 = left, top         # top of the opposite side

    ex.update(
        x0=x0, y0=y0, x1=x1, y1=y1, x2=x2, y2=y2,
        tri_w=tri_w, tri_h=tri_h,
        angle_bottom=angle_bottom, angle_top=angle_top,
        arc_r=min(tri_w, tri_h) * 0.45,
        show_bottom_first=random.choice([True, False]),
        other_revealed=False,
    )

    # Triangle
    canvas.create_polygon(
        x0, y0, x1, y1, x2, y2,
        fill="#90ee90", outline="black", width=3,
    )

    # Right-angle marker (a small square in the corner)
    marker = min(tri_w, tri_h) * 0.15
    canvas.create_rectangle(
        x0, y0 - marker, x0 + marker, y0,
        outline="black", width=2,
    )

    # Side lengths (numbers only)
    canvas.create_text((x0 + x1) / 2, y0 + 30, text=f"{adjacent}", font=("Arial", 22))
    canvas.create_text(x0 - 20, (y0 + y2) / 2, text=f"{opposite}", font=("Arial", 22),
                       anchor="e")

    # One angle is shown at the start
    draw_angle(ex["show_bottom_first"])


def inside_triangle(x, y):
    if x < ex["x0"] or y > ex["y0"]:
        return False
    # Must be on the near side of the hypotenuse
    return (x - ex["x0"]) / ex["tri_w"] + (ex["y0"] - y) / ex["tri_h"] <= 1


def on_canvas_click(event):
    if inside_triangle(event.x, event.y):
        # Inside: reveal the other angle (once)
        if not ex["other_revealed"]:
            ex["other_revealed"] = True
            draw_angle(not ex["show_bottom_first"])
    else:
        # Outside: start a new example
        new_example()


canvas.bind("<Button-1>", on_canvas_click)

new_example()
root.mainloop()