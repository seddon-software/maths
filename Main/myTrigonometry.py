import tkinter as tk
import tkinter.font
import numpy as np
from functools import partial
from math import sin, cos, tan, asin, acos, atan
from math import pi as π

precision = 2

# 2 of these must be None
ANGLE = None
OPPOSITE = 18
HYPOTENUSE = None
ADJACENT = 15

class Entity:
    def __init__(self, name, anchor):
        self.name = name
        self.anchor = anchor
        self.visible = False
    def setVisible(self):
        self.visible = True
    def getTextPosition(self):
        # return midpoint
        return tuple(T(i) for i in self.textPosition)
    def getText(self):
        if self.visible == True:
            return f"{self.size:.{precision}f}"
        else:
            return "?"

opposite = Entity('opposite', 'e')
adjacent = Entity('adjacent', 'n')
hypotenuse = Entity('hypotenuse', 'sw')
angle = Entity('angle', 'ne')

def check(x1, x2):
    def isNumber(x):
        return isinstance(x, (int, float))
    return isNumber(x1) and isNumber(x2)

if check(ANGLE, OPPOSITE):
    HYPOTENUSE = OPPOSITE / sin(ANGLE * π / 180)
    ADJACENT   = OPPOSITE / tan(ANGLE * π / 180)
    angle.setVisible()
    opposite.setVisible()

elif check(ANGLE, HYPOTENUSE):
    OPPOSITE = HYPOTENUSE / sin(ANGLE * π / 180)
    ADJACENT = HYPOTENUSE / cos(ANGLE * π / 180)
    angle.setVisible()
    hypotenuse.setVisible()

elif check(ANGLE, ADJACENT):
    OPPOSITE   = ADJACENT * tan(ANGLE * π / 180)
    HYPOTENUSE = ADJACENT / cos(ANGLE * π / 180)
    angle.setVisible()
    adjacent.setVisible()

elif check(OPPOSITE, HYPOTENUSE): # done
    ANGLE = asin(OPPOSITE / HYPOTENUSE) * 180 / π
    ADJACENT = HYPOTENUSE * cos(ANGLE * π / 180)
    opposite.setVisible()
    hypotenuse.setVisible()

elif check(OPPOSITE, ADJACENT):
    ANGLE = atan(OPPOSITE / ADJACENT) * 180 / π
    HYPOTENUSE = ADJACENT / cos(ANGLE * π / 180)
    opposite.setVisible()
    adjacent.setVisible()
else: 
    check(HYPOTENUSE, ADJACENT)
    OPPOSITE = (HYPOTENUSE**2 - ADJACENT**2)**0.5
    ANGLE = acos(ADJACENT / HYPOTENUSE) * 180 / π
    hypotenuse.setVisible()
    adjacent.setVisible()

opposite.size = OPPOSITE
adjacent.size = ADJACENT
hypotenuse.size = HYPOTENUSE
angle.size = ANGLE

opposite.textPosition = (         0, OPPOSITE/2)
adjacent.textPosition = (ADJACENT/2, OPPOSITE  )
hypotenuse.textPosition = (ADJACENT/2, OPPOSITE/2)
angle.textPosition = (ADJACENT*0.94, OPPOSITE*0.94)

def drawTriangle(adjacentEntity, oppositeEntity, hypotenuseEntity, angleEntity):
    points = (
        [T(0),T(0)], [T(0),T(oppositeEntity.size)], [T(adjacentEntity.size),T(oppositeEntity.size)]
    )
    canvas.create_polygon(*points, fill='light green')

    # add segment for angle
    x = T(ADJACENT)
    y = T(OPPOSITE)
    r = 130
    smallArcBoundingRectangle = (x-r, y-r, x+r, y+r)
    canvas.create_arc(*smallArcBoundingRectangle, start=180, extent=-ANGLE, fill="cyan")

    # add labels
    for item in oppositeEntity, adjacentEntity, hypotenuseEntity, angleEntity:
        item.id = canvas.create_text(*item.getTextPosition(), text=item.getText(), font=getFont(), anchor=item.anchor)

    canvas.create_line(T(ADJACENT*0.0), T(OPPOSITE*0.95), T(ADJACENT*0.05), T(OPPOSITE*0.95), fill="black", width=2)
    canvas.create_line(T(ADJACENT*0.05), T(OPPOSITE*0.95), T(ADJACENT*0.05), T(OPPOSITE), fill="black", width=2)
    canvas.pack()

def getFont(size=24):
    return tkinter.font.Font(family="Arial", size=size, weight=tkinter.font.NORMAL)

def T(x):   # conver to canvas coordinates
    global xMax, yMax, ADJACENT, OPPOSITE
    return 100 + x * yMax * 0.8 / max(ADJACENT,OPPOSITE)

def setGeometry(root):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{screenWidth}x{screenHeight}+0+0")

root = tk.Tk()
root.title("Trigonometry")
setGeometry(root)
canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)
root.update_idletasks()
xMax = canvas.winfo_width() - 10
yMax = canvas.winfo_height() - 10

drawTriangle(adjacent, opposite, hypotenuse, angle)

answer1 = None
answer2 = None

def displayAnswer(item):
    item.visible = True
    canvas.delete(item.id)
    canvas.create_text(*item.getTextPosition(), text=f"{item.getText()}", font=getFont(), anchor=item.anchor),

for item in opposite, adjacent, hypotenuse, angle:
    if not item.visible:
        item.visible = True
        if not answer1: 
            answer1 = item
            pfn1 = partial(displayAnswer, item)
        else:
            answer2 = item
            pfn2 = partial(displayAnswer, item)

button1 = tk.Button(
    canvas,
    text=f"{answer1.name}",
    command=pfn1,
    width=15,
    height=2, 
    bg="purple",
    fg="white",
    font=getFont()
)
button2 = tk.Button(
    canvas,
    text=f"{answer2.name}",
    command=pfn2,
    width=15,
    height=2, 
    bg="purple",
    fg="white",
    font=getFont()
)
button1.place({'x':xMax/1.5, 'y':yMax/2})
button2.place({'x':xMax/1.5, 'y':yMax/1.5})

spacing = 35
canvas.create_text(xMax/1.5, 50+0*spacing, text="sin(θ) = Opposite / Hypotenuse = O/H", font=getFont(), anchor="w")
canvas.create_text(xMax/1.5, 50+1*spacing, text="cos(θ) = Adjacent / Hypotenuse = A/H", font=getFont(), anchor="w")
canvas.create_text(xMax/1.5, 50+2*spacing, text="tan(θ) = Opposite / Adjacent = O/A", font=getFont(), anchor="w")
canvas.create_text(xMax/1.5, 50+3*spacing, text="H = √(O² + A²)", font=getFont(), anchor="w")
canvas.create_text(xMax/1.5, 50+4*spacing, text="O = √(H² - A²)", font=getFont(), anchor="w")
canvas.create_text(xMax/1.5, 50+5*spacing, text="A = √(H² - O²)", font=getFont(), anchor="w")

canvas.pack(fill="both", expand=True)

root.mainloop()