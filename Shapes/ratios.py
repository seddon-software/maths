ratio = [7, 4]
a, b = ratio
factor1 = 9
new_factor = 2
boxes1 = a * factor1
boxes2 = b * factor1
new_boxes1 = a * new_factor
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

i = max(boxes1, boxes2)
height = 800
width = 2*height
w = 0.75 * width
step1 = int(w / i)
step2 = step1 * boxes1 / boxes2

def main():    
    def solution(canvas):
        finish = False
        try:
            content = next(g)
            eval(content)
        except StopIteration as e:
            pass
    gcd = math.gcd(boxes1, boxes2)
    new_boxes2 = new_boxes1 * boxes2 / boxes1
    texts = [f"{name1} has {boxes1} yellow boxes",
             None,
             f"{name2} has {boxes2} yellow boxes",
             None,
             f"{name1} paints {new_boxes1} boxes cyan",
             None,
             f"{name2} paints boxes cyan in the same ratio",
             f"How many boxes does {name2} have to paint?",
             f"ratio is {boxes1}:{boxes2}\\n",
             f"What is the GCD of {boxes1} and {boxes2}?",
             f"The GCD of {boxes1} and {boxes2} = {gcd}",
             f"What is {boxes1}/{gcd}?",
             f"{boxes1}/{gcd} = {boxes1/gcd:.0f}",
             f"What is {boxes2}/{gcd}?",
             f"{boxes2}/{gcd} = {boxes2/gcd:.0f}",
             f"ratio is {boxes1}:{boxes2} = {boxes1/gcd:.0f}:{boxes2/gcd:.0f}",
             f"ratio is {boxes1}:{boxes2} = {boxes1/gcd:.0f}:{boxes2/gcd:.0f} = {new_boxes1}:{new_boxes2:.0f}",
             None,
             f"\\nFinished"]
    boxes = [f'drawBoxes(canvas, LEFT, {TOP}, {boxes1}, "yellow", {step1})',
             f'drawBoxes(canvas, LEFT, 2*TOP, {boxes2}, "yellow", {step2})',
             f'drawBoxes(canvas, LEFT, TOP, {new_boxes1}, "cyan", {step1})',
             f'drawBoxes(canvas, LEFT, 2*TOP, {new_boxes2}, "cyan", {step2})']
    def generator():
        texts.reverse()
        boxes.reverse()
        text = ""
        while texts:
            t = texts.pop()
            if t == None:
                yield boxes.pop()
                continue
            text += f"{t}\\n"
            yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        root.destroy()

    margin = 10
    root = tk.Tk()
    root.title("ratios")
    root.geometry(f"{width}x{height}")
    canvas = tk.Canvas(root, width=width, height=height)
    text = canvas.create_text(0, 0, text="", font="Arial 16")

    pfn = partial(solution, canvas)
    button = tk.Button(canvas, text="click", anchor="nw", command=pfn)
    canvas.create_window(RIGHT, TOP, window=button)
    canvas.pack()
    button.place(x=width-10*margin, y=TOP)

    g = generator()
    root.mainloop()

main()

