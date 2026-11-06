import tkinter as tk

class NotMultiple(Exception): pass

def is_multiple(n, k):
    return k != 0 and n % k == 0

class Ratio:
    def __init__(self, r1, r2, r3, total):
        if not is_multiple(total, r1 + r2 + r3): raise NotMultiple
        self.delta1 = r1
        self.delta2 = r2
        self.delta3 = r3
        self.ratio1 = r1
        self.ratio2 = r2
        self.ratio3 = r3
        self.total = total

    def inc(self):
        self.ratio1 += self.delta1 
        self.ratio2 += self.delta2
        self.ratio3 += self.delta3
    def dec(self):
        self.ratio1 -= self.delta1 
        self.ratio2 -= self.delta2
        self.ratio3 -= self.delta3

def callback():
    if ratio.ratio1 + ratio.ratio2 + ratio.ratio3 == ratio.total: 
        fg = "red"
    else:
        fg = "blue"
    display.config(text=f"{ratio.ratio1}:{ratio.ratio2}:{ratio.ratio3}(= {ratio.ratio1 + ratio.ratio2 + ratio.ratio3})", fg=fg)
    if hasattr(callback, "called"):
        ratio.dec()
        display2.config(text=f"{ratio.ratio1}:{ratio.ratio2}:{ratio.ratio3} (= {ratio.ratio1 + ratio.ratio2 + ratio.ratio3})", fg="blue")
        ratio.inc()
    callback.called = True
    ratio.inc()
    
##########################################################################
try:
    ratio = Ratio(5, 4, 1, total=200)
except NotMultiple as e:
    print("not multiple")
    exit(1)

root = tk.Tk()
root.title("Ratios")
root.geometry("600x400")

goal = tk.Label(root, text=f"{ratio.total} in ratio {ratio.ratio1}:{ratio.ratio2}:{ratio.ratio3}\n", font=("Arial", 24), fg="green")
goal.pack()

button = tk.Button(root, text="next", command=callback, font=("Arial", 20))
button.pack(side="bottom")

display = tk.Label(root, text=f"", font=("Arial", 20))
display.pack()

display2 = tk.Label(root, text=f"", font=("Arial", 20))
display2.pack()

root.mainloop()

