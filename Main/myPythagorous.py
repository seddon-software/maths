b = 13
a = 20

####################################################
import tkinter as tk
import tkinter.font
import numpy as np
from functools import partial

precision = 2
w = int(a + b)
scale = w / 900 
a = a/scale
b = b/scale
leftX = 200
topY = 10
margin = 10


def getFont(size=16):
    return tkinter.font.Font(family="Arial", size=size, weight=tkinter.font.NORMAL)


def main():
    def displayHypotenuse(a, b):
        c = scale*(a**2 + b**2)**0.5
        canvas.create_text(*cText, text=f"c={c:.{precision}f}", font=getFont(24), anchor="w"),

    root = tk.Tk()
    root.title("Pythagorus")
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{int(screenWidth/2)}x{int(screenHeight)}+0+0")
    canvas = tk.Canvas(root, width=screenWidth, height=screenHeight)
    canvas.pack()

    points = (
        (leftX+b, topY+a),
        (leftX, topY),
        (leftX, topY+a)
    )
    LEFT = 0.3
    buttonPlace = {"x": screenWidth*LEFT, "y": screenHeight*0.7}
    bText = (leftX*0.9+b/2, topY+a + margin)
    aText = (leftX*0.9, topY+a/2)
    cText = (leftX+b/2, topY+a/2+margin)
    legend = (screenWidth*LEFT, screenHeight*0.55)
    legend2 = (screenWidth*LEFT, screenHeight*0.6)
    canvas.create_polygon(*points, fill='light green')
    canvas.create_text(*bText, text=f"b={b*scale:.{precision}f}", font=getFont(24), anchor="w")
    canvas.create_text(*aText, text=f"a={a*scale:.{precision}f}", font=getFont(24), anchor="e")
    canvas.create_text(*cText, text=f"c", font=getFont(24), anchor="w"),
    canvas.create_text(*legend, text="c² = a² + b²", font=getFont(24), fill="red", anchor="w")
    canvas.create_text(*legend2, text="c = √(a² + b²)", font=getFont(24), fill="red", anchor="w")
    
    pfn = partial(displayHypotenuse, a, b)
    button = tk.Button(
        canvas,
        text="answer",
        command=pfn,
        width=15,
        height=2, 
        bg="purple",
        fg="white",
        font=getFont(24)
    )
    button.place(**buttonPlace)
    canvas.pack()
    root.mainloop()

main()

