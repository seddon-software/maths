radius = 10           # change this
arc = 180              # change this

#############################################################
import tkinter as tk
import numpy as np
from numpy import pi as π
from functools import partial

π = 3.14
scale = radius/150
radius = radius/scale
margin = 10
w = int(5 * radius) 
FONT = "Arial 14"
BIG_FONT = "Arial 24"

xslot1 = 0.05*w
xslot2 = 0.8*w
xslot3 = 0.25*w
xslot4 = 0.8*w
yslot = 0.8*w
π = 3.14
baseRadiusText = (0.75*w-margin, 0.50*w+2*margin)
wx = (w+radius*np.cos(arc*π/180))/2
wy = (w-radius*np.sin(arc*π/180))/2
radiusText = (wx, wy)

arcText = np.array((w/2+2*margin, w/2-margin))
areaText = (xslot2, yslot)
perimeterText = (xslot4, yslot)
area_id = None
perimeter_id = None

def main():
    def printArea(arc):
        global area_id, perimeter_id
        canvas.delete(area_id)
        canvas.delete(perimeter_id)
        r = radius*scale
        area = "A = θ/360.πr².\n"
        area += f"A = {arc/360:.3f}.πr².\n"
        area += f"r² = {r}x{r} = {r**2:.3f}\n"
        area += f"A = π x {r**2:.3f} x {arc/360:.3f}\n" 
        area += f"A = π x {r**2 * arc/360:.3f}\n" 
        area += f"A = {π * r**2 * arc / 360:.6f}"
        area_id = canvas.create_text(*areaText, text=area, font=FONT)
    def printPerimeter(arc):
        global area_id, perimeter_id
        canvas.delete(area_id)
        canvas.delete(perimeter_id)
        r = radius*scale
        p = 2 * r + 2 * π * r * arc / 360
        if arc == 360:
            perimeter = f"perimeter = 2πr\n"
            perimeter += f"πr = {π * r:.3f}\n"
            perimeter += f"2πr = 2 x {π * r:.3f}\n"
            perimeter += f"2πr = {p:.3f}\n"
            perimeter_id = canvas.create_text(*perimeterText, text=f"{perimeter}", font=FONT)
        else:
            perimeter = f"perimeter = 2r + 2πr x {arc} / 360\n"
            perimeter += f"extent = {arc} / 360 = {arc/360:.2f}\n"
            perimeter += f"P = 2r + 2πr x {arc/360:.2f}\n"
            perimeter += f"πr = {π * r:.3f}\n"
            perimeter += f"P = 2r + 2 x {π * r:.3f} x {arc/360:.2f}\n"
            perimeter += f"P = 2 x {r} + 2 x {π * r:.3f} x {arc/360:.2f}\n"
            perimeter += f"P = {2*r} + 2 x {π * r:.3f} x {arc/360:.2f}\n"
            perimeter += f"P = {2*r} + {2 * π * r:.3f} x {arc/360:.2f}\n"
            perimeter += f"P = {2*r} + {2 * π * r * arc/360:.3f}\n"
            perimeter += f"P = {p:.3f}\n"
            perimeter_id = canvas.create_text(*perimeterText, text=f"{perimeter}", font=FONT)
    root = tk.Tk()
    root.title("arcs of circle")
    root.geometry(f"{w+2*margin}x{w+2*margin}")

    canvas = tk.Canvas(root, width=w+4*margin, height=w+4*margin)
    arcBoundingRectangle = np.array((margin, margin, margin+w, margin+w))
    if arc == 360:
        canvas.create_oval(*arcBoundingRectangle, fill="red")
    else:
        canvas.create_arc(*arcBoundingRectangle, start=0, extent=arc, fill="red")
    smallArcBoundingRectangle = np.array((w/2-2*margin, w/2-2*margin, w/2+4*margin, w/2+4*margin))
    canvas.create_arc(*smallArcBoundingRectangle, start=0, extent=arc, fill="cyan")
    canvas.pack()

    canvas.create_text(baseRadiusText, text=f"r = {radius*scale}", font=BIG_FONT)
    canvas.create_text(radiusText, text=f"r = {radius*scale}", font=BIG_FONT)
    canvas.create_text(*arcText, text=f"{arc}", font=BIG_FONT)
    pfn1 = partial(printArea, arc)
    button = tk.Button(canvas, text="Area", font=FONT, command=pfn1)
    button.place(x=xslot1, y=yslot)
    pfn2 = partial(printPerimeter, arc)
    button = tk.Button(canvas, text="Perimeter", font=FONT, command=pfn2)
    button.place(x=xslot3, y=yslot)
    canvas.pack()

    root.mainloop()

main()

