hh = 3
ww = 8.2
a = 3
b = 4
c = 5

####################################################
import tkinter as tk
import tkinter.font
import numpy as np
from functools import partial


scale = .02
a = a/scale
b = b/scale
c = c/scale

leftX = 100
topY = 50
# height = hh/scale
# width = ww/scale
w = 600
slot1 = leftX+b/2, 50+a/2
# slot2 = 0.5*w
aMargin = 0.1
bMargin = b*0.1
# topY = 400
# baseY = topY + height
# topX = 100
# baseX1 = 100
# baseX2 = baseX1 + width
precision = 0
bText = (leftX*0.8+b/2, topY+a*1.1)
aText = (leftX*0.8, topY+a/2)

def getFont():
    return tkinter.font.Font(family="Arial", size=12, weight=tkinter.font.NORMAL)

def main():
    def printHypotenuse(a, b):
        c = scale*(a**2 + b**2)**0.5
        canvas.create_text(leftX+b/2, 50+a/2, text=f"c={c:.{precision}f}",
        font=getFont())

    root = tk.Tk()
    root.title("Pythagorus")
    root.geometry(f"{w}x{w}")

    canvas = tk.Canvas(root, width=w, height=w)

    points = (
        (leftX+b, topY+a),
        (leftX, topY),
        (leftX, topY+a)
    )
    canvas.create_polygon(*points, fill='cyan')
    canvas.create_text(*bText, text=f"b={b*scale:.{precision}f}", font=getFont())
    canvas.create_text(*aText, text=f"a={a*scale:.{precision}f}", font=getFont())
    # canvas.create_line(leftX*0.9, 50, leftX*0.9, 300, dash=(5,5))
#    canvas.create_line(leftX+1.5*b, 300, leftX+1.5*b, 50, dash=(5,5))
    # canvas.create_line(leftX, topY+1.1*a, leftX+b, topY+1.1*a, dash=(10,10))

    #printHypotenuse(a, b)

    pfn = partial(printHypotenuse, a, b)
    button = tk.Button(canvas, text="hypotenuse", command=pfn)
    button.place(x=leftX+b/2, y=topY+2*a)
    canvas.pack()
    root.mainloop()

main()

