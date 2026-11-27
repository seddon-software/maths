import tkinter as tk
import random

def draw_shapes():
    for _ in range(5):
        x, y = random.randint(20, 380), random.randint(20, 380)
        canvas.create_oval(x, y, x + 40, y + 40, fill="skyblue")

def on_click(event):
    # find_overlapping returns items under the click point
    if not canvas.find_overlapping(event.x, event.y, event.x, event.y):
        canvas.delete("all")   # clear the canvas
        draw_shapes()          # restart

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
canvas.bind("<Button-1>", on_click)

draw_shapes()
root.mainloop()