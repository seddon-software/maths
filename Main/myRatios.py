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
    def dec(self):
        self.ratio1 -= self.delta1 
        self.ratio2 -= self.delta2

def callback():
    global ratio, display, display2
    if ratio.ratio1 + ratio.ratio2 == ratio.total: 
        fg = "red"
    else:
        fg = "blue"
    display.config(text=f"{ratio.ratio1}:{ratio.ratio2}(= {ratio.ratio1 + ratio.ratio2})", fg=fg)
    if hasattr(callback, "called"):
        ratio.dec()
        display2.config(text=f"{ratio.ratio1}:{ratio.ratio2} (= {ratio.ratio1 + ratio.ratio2})", fg="blue")
        ratio.inc()
    callback.called = True
    ratio.inc()
    
##########################################################################
ratio = Ratio(2, 7, 81)

root = tk.Tk()
root.title("Ratios")
root.geometry("600x400")

goal = tk.Label(root, text=f"{ratio.total} in ratio {ratio.ratio1}:{ratio.ratio2}\n", font=("Arial", 24), fg="green")
goal.pack()

button = tk.Button(root, text="next", command=callback, font=("Arial", 20))
button.pack(side="bottom")

display = tk.Label(root, text=f"", font=("Arial", 20))
display.pack()

display2 = tk.Label(root, text=f"", font=("Arial", 20))
display2.pack()

root.mainloop()

