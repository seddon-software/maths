import tkinter as tk
import tkinter.font
import random
import numpy as np
from functools import partial
from math import sin, cos, tan, asin, acos, atan, degrees, radians
from math import pi as π
'''
pick opposite and adjacent
calculate hypotenuse and angle
pick 2 parameters to hide
display
'''
precision = 2
xMax = None
yMax = None



def setGeometry(root):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{screenWidth}x{screenHeight}+0+0")

def displayAnswer(canvas, item):
    item.visible = True
    canvas.delete(item.id)
    canvas.create_text(*item.getTextPosition(), text=f"{item.getText()}", font=getFont(), anchor=item.anchor),

def drawTriangle(canvas, adjacentEntity, oppositeEntity, hypotenuseEntity, angleEntity):
    points = (
        [T(0),T(0)], [T(0),T(oppositeEntity.size)], [T(adjacentEntity.size),T(oppositeEntity.size)]
    )
    canvas.create_polygon(*points, fill='light green')

    # add segment for angle
    x = T(ADJACENT)
    y = T(OPPOSITE)
    r = 130
    smallArcBoundingRectangle = (x-r, y-r, x+r, y+r)
    canvas.create_arc(*smallArcBoundingRectangle, start=180, extent=-angleEntity.size, fill="cyan")

    # add labels
    for item in oppositeEntity, adjacentEntity, hypotenuseEntity, angleEntity:
        item.id = canvas.create_text(*item.getTextPosition(), text=item.getText(), font=getFont(), anchor=item.anchor)

    canvas.create_line(T(ADJACENT*0.0), T(OPPOSITE*0.95), T(ADJACENT*0.05), T(OPPOSITE*0.95), fill="black", width=2)
    canvas.create_line(T(ADJACENT*0.05), T(OPPOSITE*0.95), T(ADJACENT*0.05), T(OPPOSITE), fill="black", width=2)
    canvas.pack()

def getFont(size=24):
    return tkinter.font.Font(family="Arial", size=size, weight=tkinter.font.NORMAL)

def T(x):   # convert to canvas coordinates
    global xMax, yMax, ADJACENT, OPPOSITE
    return 100 + x * yMax * 0.8 / max(ADJACENT,OPPOSITE)

class Entity:
    def __init__(self, name, size, anchor):
        self.name = name
        self.size = size
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

def main(root):
    global xMax, yMax, ADJACENT, OPPOSITE, HYPOTENUSE, ANGLE

    OPPOSITE = random.uniform(10, 15)
    ADJACENT = random.uniform(5, 15)
    HYPOTENUSE = (OPPOSITE**2 + ADJACENT**2) ** 0.5
    ANGLE = degrees(atan(OPPOSITE/ADJACENT))

    opposite = Entity('opposite', OPPOSITE, 'e')
    adjacent = Entity('adjacent', ADJACENT, 'n')
    hypotenuse = Entity('hypotenuse', HYPOTENUSE, 'sw')
    angle = Entity('angle', ANGLE, 'ne')

    opposite.textPosition = (         0, OPPOSITE/2)
    adjacent.textPosition = (ADJACENT/2, OPPOSITE  )
    hypotenuse.textPosition = (ADJACENT/2, OPPOSITE/2)
    angle.textPosition = (ADJACENT*0.94, OPPOSITE*0.94)

    entities = [opposite, adjacent, hypotenuse, angle]
    knowns = random.sample(entities, 2)
    unknowns = [p for p in entities if p not in knowns]

    for item in knowns:
        item.visible = True
    
    root.title("Trigonometry")
    setGeometry(root)
    canvas = tk.Canvas(root, bg="white", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    root.update_idletasks()
    xMax = canvas.winfo_width() - 10
    yMax = canvas.winfo_height() - 10

    drawTriangle(canvas, adjacent, opposite, hypotenuse, angle)

    for i, entity in enumerate(unknowns):
        pfn = partial(displayAnswer, canvas, entity.name)
        button = tk.Button(
            canvas,
            text=f"{entity.name}",
            command=partial(displayAnswer, canvas, entity),
            width=15,
            height=2, 
            bg="purple",
            fg="white",
            font=getFont()
        )
        button.place({'x':xMax/1.5, 'y':yMax/(2-i/2)})

    spacing = 35
    canvas.create_text(xMax/1.5, 50+0*spacing, text="sin(θ) = Opposite / Hypotenuse = O/H", font=getFont(), anchor="w")
    canvas.create_text(xMax/1.5, 50+1*spacing, text="cos(θ) = Adjacent / Hypotenuse = A/H", font=getFont(), anchor="w")
    canvas.create_text(xMax/1.5, 50+2*spacing, text="tan(θ) = Opposite / Adjacent = O/A", font=getFont(), anchor="w")
    canvas.create_text(xMax/1.5, 50+3*spacing, text="H = √(O² + A²)", font=getFont(), anchor="w")
    canvas.create_text(xMax/1.5, 50+4*spacing, text="O = √(H² - A²)", font=getFont(), anchor="w")
    canvas.create_text(xMax/1.5, 50+5*spacing, text="A = √(H² - O²)", font=getFont(), anchor="w")
    root.attributes("-fullscreen", True)
    # Esc exits
    root.bind("<Escape>", lambda e: root.destroy())

    canvas.pack(fill="both", expand=True)
    canvas.bind("<Button-1>", lambda event: on_click(event, canvas, root))
    return canvas, root

def on_click(event, canvas, root):
    if not canvas.find_overlapping(
        event.x, event.y, event.x, event.y
    ):
        canvas.destroy()       # removes canvas AND its buttons
        root.after(0, main, root)  # create a fresh display

    return "break"

root = tk.Tk()
main(root)
root.mainloop()








