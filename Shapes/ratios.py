a = 5
b = 4
c = 9
d = 2
item1 = a * c
item2 = b * c
newItem1 = a * d
name1 = "George"
name2 = "Peter"

########################################
import tkinter as tk
import numpy as np
from functools import partial

LEFT = 50
RIGHT = 1000
TOP = 50

def drawBoxes(canvas, baseX, baseY, n, color, step):
    ystep = 26
    for n, x0 in enumerate(np.arange(baseX, baseX+n*step, step)):
        x1 = x0 + step
        y0 = baseY
        y1 = y0 + ystep
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text(x0+step//2, y0+ystep//2, text=f"{n+1}")

def create_text(canvas, x, y, text, anchor, font):
    return canvas.create_text(x, y, text=text, anchor=anchor, font=font)

i = max(item1, item2)
height = 800
step1 = height / i
step2 = height * item1 / (i * item2)

def main():    
    def solution():
        nonlocal text, canvas
        finish = False
        try:
            content = next(g)
            eval(content)
        except StopIteration as e:
            pass

    def generator():
        text = f"{name1} is {item1}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, TOP, item1, "yellow", {step1})'
        text += f"{name2} is {item2}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, 2*TOP, item2, "yellow", {step2})'
        text += f"{name1} becomes {newItem1}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, TOP, newItem1, "cyan", {step1})'
        text += f"ratio is {item1}:{item2}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"ratio is {item1}:{item2} = {item1} / {item2}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        item2B = item2*newItem1//item1
        text += f"ratio is {item1}:{item2} = {item1} / {item2} = {newItem1} / ???\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"??? =  {newItem1} ÷ ({item1}/{item2})\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"??? =  {newItem1} * {item2} ÷ {item1}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"??? = {item2 * newItem1} / {item1}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"??? = {item2 * newItem1 // item1}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"equivalent ratio is {newItem1}:???\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"equivalent ratio is {newItem1}:{item2B}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, 2*TOP, {item2B}, "cyan", {step2})'
        text += f"\\nFinished\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        return

    margin = 10
    root = tk.Tk()
    root.title("ratios")
    width = 2*height
    root.geometry(f"{width}x{height}")
    canvas = tk.Canvas(root, width=width, height=height)
    text = canvas.create_text(0, 0, text="", font="Arial 16")

    button = tk.Button(canvas, text="click", command=solution)
    button.pack()
    canvas.create_window(RIGHT, TOP, window=button)
    canvas.pack()

    g = generator()
    root.mainloop()

main()

