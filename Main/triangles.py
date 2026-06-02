hh = 8.2
ww = 1.6

####################################################
import tkinter as tk
import numpy as np
from functools import partial
from fonts import getFont
import multiplyBoxes

def displayMultiplyBoxes(h, w):
    multiplyBoxes.main(int(h), int(w))


scale = .02
height = hh/scale
width = ww/scale
w = 600
slot1 = 0.3*w
slot2 = 0.5*w
margin = 10
topY = 100
baseY = topY + height
topX = 400
baseX1 = 100
baseX2 = baseX1 + width
middleText = (topX, baseX1 + width/2)
baseText = ((baseX2 + baseX1)/2, baseY+margin)


def main():
    def printArea(height, width):
        area = height * width * scale**2 / 2
        canvas.create_text(slot2, w-0.5*margin, text=f"{area:.2f}",
        font=getFont())

    root = tk.Tk()
    root.title("triangles")
    root.geometry(f"{w+2*margin}x{w+2*margin}")
    # Create fonts with different weights and slants
#    f = tkFont.Font(family="Arial", size=24, weight=tkFont.NORMAL)

    canvas = tk.Canvas(root, width=w+4*margin, height=w+4*margin)

    points = (
        (baseX1, baseY),
        (baseX2, baseY),
        (topX, topY)
    )
    canvas.create_polygon(*points, fill='cyan')
    canvas.create_line(topX, topY, topX, baseY, dash=(10,10))
    canvas.create_text(*middleText, text=f"{height*scale}", font=getFont())
    canvas.create_text(*baseText, text=f"{width*scale}", font=getFont())
    pfn1 = partial(printArea, height, width)
    button = tk.Button(canvas, text="Area", command=pfn1)
    button.place(x=slot1, y=w-2*margin)
    canvas.pack()

    root.mainloop()

    displayMultiplyBoxes(hh*10, ww*10)

main()

