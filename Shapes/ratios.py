a = 7
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
import math

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
width = 2*height
w = 0.75 * width
step1 = int(w / i)
step2 = step1 * item1 / item2
print(step1, step2)

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
        text = f"{name1} has {item1} yellow boxes\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, TOP, item1, "yellow", {step1})'
        text += f"{name2} has {item2} yellow boxes\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, 2*TOP, item2, "yellow", {step2})'
        text += f"{name1} paints {newItem1} boxes cyan\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, TOP, newItem1, "cyan", {step1})'
        text += f"{name2} paints boxes cyan in the same ratio\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"How many boxes does {name2} have to paint?\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"ratio is {item1}:{item2}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"What is the GCD of {item1} and {item2}?\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        gcd = math.gcd(item1, item2)
        text += f"The GCD of {item1} and {item2} = {gcd}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"What is {item1}/{gcd}?\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"{item1}/{gcd} = {item1/gcd:.0f}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"What is {item2}/{gcd}?\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"{item2}/{gcd} = {item2/gcd:.0f}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"ratio is {item1}:{item2} = {item1/gcd:.0f}:{item2/gcd:.0f}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        newItem2 = newItem1 * item2 / item1
        text += f"ratio is {item1}:{item2} = {item1/gcd:.0f}:{item2/gcd:.0f} = {newItem1}:{newItem2:.0f}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, 2*TOP, {newItem2}, "cyan", {step2})'
        text += f"\\nFinished\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        return

    margin = 10
    root = tk.Tk()
    root.title("ratios")
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

