n1 = 736
n2 = 451

#############################################################
import tkinter as tk
import numpy as np
from numpy import pi as π
from functools import partial
FONT = "Arial 32"

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
        self.value = n
    def size(self):
        return len(f"{self.n}")     # for the decimal point
    def __getitem__(self, index):
        return self.n[index]
    def getValue(self):
        return self.value
       
class Box:
    def __init__(self, x1, y1, row, col):
        self.x1 = x1
        self.y1 = y1
        self.number1 = row
        self.number2 = col
        self.x2 = x1 + self.number2.size()*space
        self.y2 = y1 + self.number1.size()*space
    def drawOutline(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y1, width=2)
        canvas.create_line(self.x1, self.y1, self.x1, self.y2, width=2)
        canvas.create_line(self.x2, self.y2, self.x2, self.y1, width=2)
        canvas.create_line(self.x2, self.y2, self.x1, self.y2, width=2)
    def drawInside(self, canvas):
        # height = rows * space 
        # width  = cols * space
        rows = self.number1.size()      # 3
        cols = self.number2.size()      # 2
        # horizontal lines
        for c in range(rows):
            canvas.create_line(self.x1, self.y1+c*space, self.x2, self.y1+c*space, width=1)
        # vertical lines
        for r in range(cols):
            canvas.create_line(self.x1+r*space, self.y1, self.x1+r*space, self.y2, width=1)

        # headings
        for c in range(cols):
            n2 = int(self.number2[c])
            canvas.create_text(self.x1+(c+0.5)*space, self.y1-space/2, text=f"{n2}", font=FONT)
        for r in range(rows):
            n1 = int(self.number1[r])
            canvas.create_text(self.x1-space/2, self.y1+(r+0.5)*space, text=f"{n1}", font=FONT)
        # diagonal lines
        for c in range(cols):
            n2 = int(self.number2[c])
            x1 = self.x1 + c*space
            y1 = self.y1
            x2 = x1 + space
            for r in range(rows):
                n1 = int(self.number1[r])
                y1 = self.y1 + r*space
                y2 = y1 + space
                canvas.create_line(x2, y1, x1, y2, width=1)
                # internal numbers
                canvas.create_text(x1+space/4, y1+space/2, text=f"{n1*n2//10}", font=FONT)
                canvas.create_text(x1+3*space/4, y1+space/2, text=f"{n1*n2%10}", font=FONT)
    def printResult(self, canvas):
        n1 = self.number1.getValue()
        n2 = self.number2.getValue()
        rows = self.number1.size()
        cols = self.number2.size()
        canvas.create_text(self.x1+0.5*space, self.y1+(rows+0.5)*space, text=f"{n1*n2}", font=FONT)

def main():
    root = tk.Tk()
    root.title("Multiply")
    root.geometry(f"{w+2*margin}x{w+2*margin}")
    canvas = tk.Canvas(root, width=w+4*margin, height=w+4*margin)
    number1= Number(n1)
    number2= Number(n2)
    box = Box(250, 100, row=number1, col=number2)
    box.drawOutline(canvas)
    box.drawInside(canvas)
    box.printResult(canvas)
    canvas.pack()
    root.mainloop()

main()

