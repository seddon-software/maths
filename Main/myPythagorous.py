a = 3.2
b = 6.7

####################################################
import tkinter as tk
import tkinter.font
import numpy as np
from functools import partial

precision = 2
scale = .01
a = a/scale
b = b/scale
leftX = 200
topY = 50
bText = (leftX*0.8+b/2, topY+a*1.1)
aText = (leftX*0.8, topY+a/2)
legend = (leftX+b/4, topY+a*1.5)
legend2 = (leftX+b/4, topY+a*1.65)
buttonPlace = {"x": leftX+b/4, "y": topY+2*a}


def getFont(size=16):
    return tkinter.font.Font(family="Arial", size=size, weight=tkinter.font.NORMAL)


def main():
    def printHypotenuse(a, b):
        c = scale*(a**2 + b**2)**0.5
        canvas.create_text(leftX+b/2, 50+a/2, text=f"c={c:.{precision}f}",
        font=getFont())

    root = tk.Tk()
    root.title("Pythagorus")
    w = int(a + b)
    root.geometry(f"{w}x{w}")

    canvas = tk.Canvas(root, width=w, height=w)

    points = (
        (leftX+b, topY+a),
        (leftX, topY),
        (leftX, topY+a)
    )
    canvas.create_polygon(*points, fill='light green')
    canvas.create_text(*bText, text=f"b={b*scale:.{precision}f}", font=getFont())
    canvas.create_text(*aText, text=f"a={a*scale:.{precision}f}", font=getFont())
    canvas.create_text(*legend, text="c² = a² + b²", font=getFont(24), anchor="w")
    canvas.create_text(*legend2, text="c = √(a² + b²)", font=getFont(24), anchor="w")
    
    
    pfn = partial(printHypotenuse, a, b)
    button = tk.Button(
        canvas,
        text="hypotenuse",
        command=pfn,
        width=15,
        height=2, 
        bg="purple",
        fg="white",
        font=getFont()
    )
    button.place(**buttonPlace)
    canvas.pack()
    root.mainloop()

main()

