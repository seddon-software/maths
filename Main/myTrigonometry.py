import tkinter as tk
import tkinter.font
import numpy as np
from functools import partial
from math import sin, cos, tan, asin, acos, atan
from math import pi as π

precision = 2

# 2 of these must be None
angle = None
opposite = 10
hypotenuse = None
adjacent = 4

class Entity:
    def __init__(self, name, anchor):
        self.name = name
        self.anchor = anchor
        self.visible = False
    def setVisibile(self):
        self.visible = True
    def getTextPosition(self):
        # return midpoint
        return tuple(T(i) for i in self.textPosition)
    def getText(self):
        if self.visible == True:
            return f"{self.size:.{precision}f}"
        else:
            return "?"

oppositeEntity = Entity('opposite', 'e')
adjacentEntity = Entity('adjacent', 'n')
hypotenuseEntity = Entity('hypotenuse', 'sw')
angleEntity = Entity('angle', 'ne')

def check(x1, x2):
    def isNumber(x):
        return isinstance(x, (int, float))
    return isNumber(x1) and isNumber(x2)

if check(angle, opposite):
    hypotenuse = opposite / sin(angle * π / 180)
    adjacent   = opposite / tan(angle * π / 180)
    angleEntity.setVisibile()
    oppositeEntity.setVisibile()

elif check(angle, hypotenuse):
    opposite = hypotenuse / sin(angle * π / 180)
    adjacent = hypotenuse / cos(angle * π / 180)
    angleEntity.setVisibile()
    hypotenuseEntity.setVisibile()

elif check(angle, adjacent):
    opposite   = adjacent * tan(angle * π / 180)
    hypotenuse = adjacent / cos(angle * π / 180)
    angleEntity.setVisibile()
    adjacentEntity.setVisibile()

elif check(opposite, hypotenuse): # done
    angle = asin(opposite / hypotenuse) * 180 / π
    adjacent = hypotenuse * cos(angle * π / 180)
    oppositeEntity.setVisibile()
    hypotenuseEntity.setVisibile()

elif check(opposite, adjacent):
    angle = atan(opposite / adjacent) * 180 / π
    hypotenuse = adjacent / cos(angle * π / 180)
    oppositeEntity.setVisibile()
    adjacentEntity.setVisibile()
else: 
    check(hypotenuse, adjacent)
    opposite = (hypotenuse**2 - adjacent**2)**0.5
    angle = acos(adjacent / hypotenuse) * 180 / π
    hypotenuseEntity.setVisibile()
    adjacentEntity.setVisibile()

oppositeEntity.size = opposite
adjacentEntity.size = adjacent
hypotenuseEntity.size = hypotenuse
angleEntity.size = angle

oppositeEntity.textPosition = (         0, opposite/2)
adjacentEntity.textPosition = (adjacent/2, opposite  )
hypotenuseEntity.textPosition = (adjacent/2, opposite/2)
angleEntity.textPosition = (adjacent*0.94, opposite*0.94)

def drawTriangle(adjacentEntity, oppositeEntity, hypotenuseEntity, angleEntity):
    points = (
        [T(0),T(0)], [T(0),T(oppositeEntity.size)], [T(adjacentEntity.size),T(oppositeEntity.size)]
    )
    canvas.create_polygon(*points, fill='light green')

    # add labels
    for item in oppositeEntity, adjacentEntity, hypotenuseEntity, angleEntity:
        item.id = canvas.create_text(*item.getTextPosition(), text=item.getText(), font=getFont(), anchor=item.anchor)
    
    # add segment for angle
    x = T(adjacent)
    y = T(opposite)
    r = 130
    smallArcBoundingRectangle = (x-r, y-r, x+r, y+r)
    canvas.create_arc(*smallArcBoundingRectangle, start=180, extent=-angle, fill="cyan")
    canvas.pack()

def getFont(size=24):
    return tkinter.font.Font(family="Arial", size=size, weight=tkinter.font.NORMAL)

def T(x):   # conver to canvas coordinates
    global xMax, yMax, adjacent, opposite
    return 100 + x * yMax * 0.8 / max(adjacent,opposite)

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

drawTriangle(adjacentEntity, oppositeEntity, hypotenuseEntity, angleEntity)

answer1 = None
answer2 = None

def displayAnswer(item):
    item.visible = True
    canvas.delete(item.id)
    canvas.create_text(*item.getTextPosition(), text=f"{item.getText()}", font=getFont(), anchor=item.anchor),

for item in oppositeEntity, adjacentEntity, hypotenuseEntity, angleEntity:
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

root.mainloop()