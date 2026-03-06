n1 = 314
n2 = 65

#############################################################
import tkinter as tk
import numpy as np
from numpy import pi as π
from functools import partial


w = 800
margin = 10
space = 100
slot1 = 0.2*w
slot2 = 0.45*w
slot3 = 0.55*w
slot4 = 0.9*w
π = 3.14

class Number:
    def __init__(self, n):
        self.n = f"{n}"
    def size(self):
        return len(f"{self.n}") - 1     # for the decimal point
    def __getitem__(self, index):
        return self.n[index]
    
class Box:
    def __init__(self, x1, y1, rows, cols):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + cols*space
        self.y2 = y1 + rows*space
        self.rows = rows
        self.cols = cols
    def drawOutline(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y1, width=2)
        canvas.create_line(self.x1, self.y1, self.x1, self.y2, width=2)
        canvas.create_line(self.x2, self.y2, self.x2, self.y1, width=2)
        canvas.create_line(self.x2, self.y2, self.x1, self.y2, width=2)
    def drawInside(self, canvas, rows, cols):
        height = rows * space 
        width  = cols * space

        # horizontal lines
        for r in range(rows):
            canvas.create_line(self.x1, self.y1+r*space, self.x2, self.y1+r*space, width=1)
        # vertical lines
        for c in range(cols):
            canvas.create_line(self.x1+c*space, self.y1, self.x1+c*space, self.y2, width=1)
        # diagonal lines
        for r in range(cols):
            x1 = self.x1 + r*space
            x2 = x1 + space
            for c in range(rows):
                y1 = self.y1 + c*space
                y2 = y1 + space
                canvas.create_line(x1, y1, x2, y2, width=1)
                canvas.create_text(x1+space/4, y1+space/2, text="?")
                canvas.create_text(x1+3*space/4, y1+space/2, text="?")


def main():
    root = tk.Tk()
    root.title("Multiply")
    root.geometry(f"{w+2*margin}x{w+2*margin}")

    canvas = tk.Canvas(root, width=w+4*margin, height=w+4*margin)
    number1= Number(n1)
    number2= Number(n2)
    print(number1[2])
    box = Box(250, 100, rows=3, cols=2)
    box.drawOutline(canvas)
#    box.drawInside(canvas, rows=number1.size(), cols=number2.size())
    box.drawInside(canvas, rows=3, cols=2)

    canvas.pack()
    root.mainloop()

main()

