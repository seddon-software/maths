hh = 2.9
ww = 3.8

########################################
import tkinter as tk
import numpy as np
from functools import partial
from fonts import getFont


scale = .02
height = hh/scale
width = ww/scale
w = 600
margin = 10
xLeft = 100
yTop = 100
xRight = xLeft + width
yBottom = yTop + height
sideText = (xLeft - margin, (yTop + yBottom)/2)
baseText = ((xLeft + xRight)/2, yBottom+margin)

slot1 = 0.2*w
slot2 = 0.45*w
slot3 = 0.6*w
slot4 = 0.85*w

import multiplyBoxes

def displayMultiplyBoxes(h, w):
    multiplyBoxes.main(int(h), int(w))

def main():
    def printArea(height, width):
        area = height * width
        canvas.create_text(slot2, w-0.5*margin, text=f"{area:.2f}", font=getFont())
    def printPerimeter(height, width):
        perimeter = 2*(height + width)
        canvas.create_text(slot4, w-0.5*margin, text=f"{perimeter:.2f}", font=getFont())
    
    root = tk.Tk()
    root.title("rectangles")
    root.geometry(f"{w+2*margin}x{w+2*margin}")

    canvas = tk.Canvas(root, width=w+4*margin, height=w+4*margin)

    points = (
        (xLeft, yTop),
        (xLeft, yBottom),
        (xRight, yBottom),
        (xRight, yTop)
    )
    canvas.create_polygon(*points, fill='yellow')
    canvas.create_text(*sideText, text=f"{height*scale:.1f}", font=getFont())
    canvas.create_text(*baseText, text=f"{width*scale:.1f}", font=getFont())
    pfn1 = partial(printArea, height*scale, width*scale)
    button = tk.Button(canvas, text="Area", command=pfn1)
    button.place(x=slot1, y=w-2*margin)
    pfn2 = partial(printPerimeter, height*scale, width*scale)
    button = tk.Button(canvas, text="Perimeter", command=pfn2)
    button.place(x=slot3, y=w-2*margin)
    canvas.pack()

    root.mainloop()

    displayMultiplyBoxes(hh*10, ww*10)

main()

