angle = 37

####################################################
import tkinter as tk
import tkinter.font
import numpy as np
from functools import partial

precision = 0
# uppercase unscaled
O = 4
A = 3
H = 5
w = int(O + A)
scale = w / 900

# lowercase scaled
o = O/scale
a = A/scale
h = H/scale
leftX = 200
topY = 10
margin = 10

class Side:
    def __init__(self, length, name, p1, p2, anchor):
        self.length = length
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.anchor = anchor
    def getPosition(self):
        return self.p1
    def getTextPosition(self):
        # return midpoint
        return tuple((x + y)/2 for x, y in zip(self.p1, self.p2))

def getFont(size=24):
    return tkinter.font.Font(family="Arial", size=size, weight=tkinter.font.NORMAL)


def main():
    def displayAnswer(a, b):
        c = scale*(a**2 + b**2)**0.5
        canvas.create_text(*cText, text=f"c={c:.{precision}f}", font=getFont(24), anchor="w"),

    root = tk.Tk()
    root.title("Trigonometry")
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{int(screenWidth/2)}x{int(screenHeight)}+0+0")
    canvas = tk.Canvas(root, width=screenWidth, height=screenHeight)
    canvas.pack()
    adjacent = Side(length=A, name='a' , p1=(leftX, topY+o), p2=(leftX+a, topY+o), anchor='w')
    opposite = Side(length=O, name='o' , p1=(leftX+a, topY), p2=(leftX+a, topY+o), anchor='w')
    hypotenuse = Side(length=H, name='h' , p1=(leftX+a, topY+o), p2=(leftX, topY), anchor='s')

    points = (
        adjacent.getPosition(),
        opposite.getPosition(),
        hypotenuse.getPosition(),
    )
    buttonPosition = {"x": 0.3*screenWidth, "y": screenHeight*0.7}
    angleText = (leftX+a*0.2, topY+o*0.97)
    canvas.create_polygon(*points, fill='light green')
    for side in opposite, adjacent, hypotenuse:
        canvas.create_text(*side.getTextPosition(), text=f"{side.name}={side.length:.{precision}f}", font=getFont(), anchor=side.anchor)

    canvas.create_text(*angleText, text=f"{angle}\N{DEGREE SIGN}", font=getFont(), anchor="e"),
    # legend = (0.3*screenWidth, screenHeight*0.55)
    # legend2 = (0.3*screenWidth, screenHeight*0.6)
    # canvas.create_text(*legend, text="c² = a² + b²", font=getFont(), fill="red", anchor="w")
    # canvas.create_text(*legend2, text="c = √(a² + b²)", font=getFont(), fill="red", anchor="w")
    
    pfn = partial(displayAnswer, O, A)
    button = tk.Button(
        canvas,
        text="answer",
        command=pfn,
        width=15,
        height=2, 
        bg="purple",
        fg="white",
        font=getFont()
    )
    button.place(**buttonPosition)
    canvas.pack()
    root.mainloop()

main()

