n1 = 4
n2 = 8

########################################
import tkinter as tk
import numpy as np
from functools import partial
import math



def main():    
    root = tk.Tk()
    root.title("ratios")
    root.geometry(f"1200x600")

    canvas = tk.Canvas(root, width=1200, height=800)
    lcm = math.lcm(n1, n2)
    for ii, x in enumerate(range(100, 1101, 50)):
        i = ii+1
        if n1*i == lcm:
            canvas.create_text(x, 100, text=f"{n1*i}", font="Arial 32 bold", fill="red")
        else:
            canvas.create_text(x, 100, text=f"{n1*i}", font="Arial 16")
        if n2*i == lcm:
            canvas.create_text(x, 200, text=f"{n2*i}", font="Arial 32 bold", fill="red")
        else:
            canvas.create_text(x, 200, text=f"{n2*i}", font="Arial 16")

    canvas.pack()

    root.mainloop()


main()

