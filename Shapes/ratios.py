item1 = 20
item2 = 15
item1B = 12

########################################
import tkinter as tk
import numpy as np
from functools import partial

# ratio1 = 5
# ratio2 = 3
w = 600
margin = 10
step = 40
LEFT = 50
RIGHT = 1000
TOP = 50
x_text = 500
y_text = 500

def drawBoxes(canvas, baseX, baseY, n, color):
    for n, x0 in enumerate(range(baseX, baseX+n*step, step)):
        x1 = x0 + step
        y0 = baseY
        y1 = y0 + step
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text(x0+step//2, y0+step//2, text=f"{n+1}")

def create_text(canvas, x, y, text, anchor, font):
    print(text)
    return canvas.create_text(x, y, text=text, anchor=anchor, font=font)

def main():    
    root = tk.Tk()
    root.title("ratios")
    height = w+2*margin
    width = 2*w+2*margin
    root.geometry(f"{width}x{height}")
    canvas = tk.Canvas(root, width=width, height=height)

    def generator():
        text = f"item1 is {item1}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, TOP, item1, "yellow")'
        text += f"item2 is {item2}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, 2*TOP, item2, "yellow")'
        text += f"item1 becomes {item1B}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, TOP, item1B, "cyan")'
        text += f"ratio is {item1}:{item1B}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        text += f"equivalent ratio is {item1B}:???\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        item2B = item2*item1B//item1
        text += f"equivalent ratio is {item1B}:{item2B}\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        yield f'drawBoxes(canvas, LEFT, 2*TOP, {item2B}, "cyan")'
        text += f"FINISHED\\n"
        yield f'create_text(canvas, LEFT, 4*TOP, text="{text}", anchor="nw", font="Arial 18")'
        return

    g = generator()
    n = 1.0
    content = ""
    text = canvas.create_text(0, 0, text="", font="Arial 16")
    
    def solution():
        nonlocal text, n, content, canvas
        finish = False
        try:
            content = next(g)
            print(content)
            eval(content)
        except StopIteration as e:
            pass

    button = tk.Button(canvas, text="click", command=solution)
    button.pack()
    canvas.create_window(RIGHT, TOP, window=button)
    canvas.pack()

    root.mainloop()


main()

