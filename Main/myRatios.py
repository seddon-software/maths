import tkinter as tk

class Ratio:
    def __init__(self, r1, r2, total):
        self.delta1 = r1
        self.delta2 = r2
        self.ratio1 = r1
        self.ratio2 = r2
        self.total = total

    def inc(self):
        self.ratio1 += self.delta1 
        self.ratio2 += self.delta2

def callback():
    global ratio, display
    display.config(text=f"{ratio.ratio1}:{ratio.ratio2} ({ratio.ratio1 + ratio.ratio2})")
    if ratio.ratio1 + ratio.ratio2 > ratio.total: root.destroy()
    ratio.inc()

##########################################################################
ratio = Ratio(3, 8, 99)

root = tk.Tk()
root.geometry("600x400")

goal = tk.Label(root, text=f"{ratio.total} in ratio {ratio.ratio1}:{ratio.ratio2}", font=("Arial", 24))
goal.pack()

button = tk.Button(root, text="next", command=callback, font=("Arial", 24))
button.pack(side="bottom")

display = tk.Label(root, text=f"", font=("Arial", 24))
display.pack()

root.mainloop()

