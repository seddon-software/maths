import tkinter as tk
from tkinter import Canvas
import math
import numpy as np

N = 13
D = 8

w = 1200
h = 800
r = 200
margin = 10
M = N - D
fraction = f"{N}/{D}"

def draw_pie_chart(canvas, x, y, r, D, M):
    for i, angle in enumerate(np.linspace(0, 360, D+1)):
        if i < M: 
            canvas.create_arc(
                            x - r, y - r, x + r, y + r,
                            start=angle,
                            extent=360/D,
                            fill=f'cyan',
                            outline='black',
                            width=2)
    for i, angle in enumerate(np.linspace(90, 360+90, D+1)):
        angle -= 180/D
        X = x + r * np.sin(angle*np.pi/180) / 2
        Y = y + r * np.cos(angle*np.pi/180) / 2 
        if i <= M and i != 0: 
            canvas.create_text(X, Y, text=f"{i}", fill="black", font="Arial 16")
            
def on_draw_click():
    draw_pie_chart(canvas, r+margin, r+margin, r, D, D)
    draw_pie_chart(canvas, 3*(r+margin), r+margin, r, D, M)
    canvas.create_text(r+margin, 2.1*(r+margin), text=f"1 = {D}/{D}", fill="red", font="Arial 32")
    canvas.create_text(3*(r+margin), 2.1*(r+margin), text=f"{N}/{D} = 1 + {M}/{D}", fill="red", font="Arial 32")
root = tk.Tk()
root.title(f"{N}/{D}")
root.geometry(f"{w}x{h}")

button = tk.Button(root, text="click", command=on_draw_click)
button.pack(pady=margin)

canvas = Canvas(root, bg='white', width=w, height=h)
canvas.pack()

root.mainloop()