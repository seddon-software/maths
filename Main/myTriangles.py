hh = 4.5
ww = 8.2

####################################################
import tkinter as tk
import tkinter.font as tkfont
import numpy as np
from functools import partial
import multiplyBoxes

def displayMultiplyBoxes(h, w):
    multiplyBoxes.main(int(h), int(w))


scale = .02
height = hh/scale
width = ww/scale
w = 600
margin = 10
topY = 100
baseY = topY + height
topX = 400
baseX1 = 100
baseX2 = baseX1 + width
buttonText = {'x':0.3*w, 'y':w-2*margin}
areaText = (0.5*w, w-0.5*margin)
middleText = (topX, baseX1 + width/2)
baseText = ((baseX2 + baseX1)/2, baseY+margin)


def main():
    def getFont():
        return tkfont.Font(family="Arial", size=24, weight=tkfont.NORMAL)

    def printArea(height, width):
        area = height * width * scale**2 / 2
        canvas.create_text(*areaText, text=f"{area:.2f}", font=getFont())

    root = tk.Tk()
    root.title("triangles")
    root.geometry(f"{w+2*margin}x{w+2*margin}")

    canvas = tk.Canvas(root, width=w+4*margin, height=w+4*margin)

    points = (
        (baseX1, baseY),
        (baseX2, baseY),
        (topX, topY)
    )
    canvas.create_polygon(*points, fill='cyan')
    canvas.create_line(topX, topY, topX, baseY, dash=(10,10))   # vertical dashed line
    canvas.create_text(*middleText, text=f"{height*scale:2.1f}", font=getFont())
    canvas.create_text(*baseText, text=f"{width*scale:2.1f}", font=getFont())
    pfn1 = partial(printArea, height, width)
    button = tk.Button(canvas, text="Area", command=pfn1)
    button.place(**buttonText)
    canvas.pack()

    root.mainloop()

    displayMultiplyBoxes(hh*10, ww*10)

main()

