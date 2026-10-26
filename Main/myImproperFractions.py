import tkinter as tk
from tkinter import Canvas
import math
import numpy as np

# display N/D in pies
N = 31
D = 7
pies = N // D
fraction = N - D * pies
w = 1200
h = 800
r = 100
margin = 10
FONT_SIZE = 20

def draw_pie_chart(canvas, x, y, r, D, M, n = 1):
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
        X = x + 1.5*r * np.sin(angle*np.pi/180) / 2
        Y = y + 1.5*r * np.cos(angle*np.pi/180) / 2 
        if i <= M and i != 0: 
            canvas.create_text(X, Y, text=f"{i}", fill="black", font="Arial 8")
            
def on_draw_click():
    for n in range(pies+1):
        nn = 2*n + 1
        if n != pies: 
            draw_pie_chart(canvas, nn*(r+margin), r+margin, r, D, D)
            canvas.create_text(nn*(r+margin), 2.1*(r+margin), text=f"{(n+1)*D}/{D} = {n+1}", fill="blue", font=FONT_SIZE)
        else:
            draw_pie_chart(canvas, nn*(r+margin), r+margin, r, D, fraction)
            canvas.create_text(nn*(r+margin), 2.1*(r+margin), text=f"{N}/{D} = {n+1} + {fraction}/{D}", fill="red", font=FONT_SIZE)

root = tk.Tk() 
root.title("Improper Fractions")
root.geometry(f"{w}x{h}")
goal = tk.Label(root, text=f"{N}/{D}\n", font=("Arial", 24), fg="green")
goal.pack()

button = tk.Button(root, text="click", command=on_draw_click)
button.pack(pady=margin)

canvas = Canvas(root, bg='white', width=w, height=h)
canvas.pack()

root.mainloop()