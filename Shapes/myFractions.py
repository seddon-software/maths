# fractions only
f1 = "1/10"
f2 = "3/4"

import tkinter as tk
import math
from fractions import Fraction
from math import gcd

def color_text(widget, target, tag_name, **tag_options):
    # Create/update tag style
    widget.tag_config(tag_name, **tag_options)
    start = "1.0"
    while True:
        pos = widget.search(target, start, stopindex="end")
        if not pos: break
        end = f"{pos} lineend"
        widget.tag_add(tag_name, pos, end)
        start = end

class FractionCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fraction Addition Calculator")
        self.root.geometry("800x800")
        
        self.stage = 0
        self.f1 = f1
        self.f2 = f2
        self.f1_n = Fraction(f1).numerator
        self.f1_d = Fraction(f1).denominator
        self.f2_n = Fraction(f2).numerator
        self.f2_d = Fraction(f2).denominator
        self.d = math.lcm(self.f1_d, self.f2_d)

        self.text_display = tk.Text(root, width=60, height=30, font=("Courier", 16, "bold"))
        self.text_display.pack(pady=5)
        
        self.button = tk.Button(root, text="Next Stage", command=self.show_next_stage, font=("Arial", 16))
        self.button.pack()
        
        self.show_stage()
    
    def show_stage(self):
        self.text_display.delete(1.0, tk.END)
        content = ""
        
        if self.stage >= 0:
            content += f"Step 1: Add the fractions\n"
            content += f"{self.f1} + {self.f2}\n\n"
        
        if self.stage >= 1:
            content += f"Step 2: Find the new denominator\n"
            d = self.f1_d * self.f2_d
    
        if self.stage >= 2:
            content += f"Denominator = {d}\n\n"

        if self.stage >= 3:
            content += f"Step 3: Convert to equivalent fractions\n"
            f1n = int(self.f1_n*d/self.f1_d)
            f2n = int(self.f2_n*d/self.f2_d)
            f1 = Fraction(f1n, d, _normalize=False)
            f2 = Fraction(f2n, d, _normalize=False)
            content += f"{self.f1} = ???/{d}\n"
        if self.stage >= 4:
            content += f"{self.f1} = {f1}\n"
        if self.stage >= 5:
            content += f"{self.f2} = ???/{d}\n"
        if self.stage >= 6:
            content += f"{self.f2} = {f2}\n\n"
        
        if self.stage >= 7:
            content += f"Step 4: Add the numerators\n"
            result = Fraction(f1n+f2n, d, _normalize=False)

        if self.stage >= 8:
            numerator2 = f1n + f2n
            content += f"{f1} + {f2} = ???/{d}\n"
        if self.stage >= 9:
            content += f"{f1} + {f2} = {result}\n\n"
        
        if self.stage >= 10:
                content += f"Step 5: Reduce fraction\n"
                content += f"{result} = ???\n"
        if self.stage >= 11:

                numerator = numerator2
                denominator = d

                g = gcd(numerator, denominator)

                numerator //= g
                denominator //= g

                reducedFraction = f"{numerator}/{denominator}"

                content += f"{result} = {reducedFraction}\n\n"

        if self.stage >= 12:
            if result > 1:
                whole = int(result)
                fraction = result - whole
                content += f"Step 6: Normalise\n"
        
        if self.stage >= 13:
            if result > 1:
                content += f"{reducedFraction} = {whole} + ???/{denominator}\n"
        if self.stage >= 14:
            if result > 1:

                content += f"{reducedFraction} = {whole} {numerator-denominator}/{denominator}\n\n"

        if self.stage >= 14:
            content += f"Finished\n"

        self.text_display.insert(1.0, content, "red")
        color_text(self.text_display, "Step", "red_tag", foreground="red")
        self.text_display.config(state=tk.DISABLED)
    
    def show_next_stage(self):
        if self.stage < 14:
            self.stage += 1
            self.text_display.config(state=tk.NORMAL)
            self.show_stage()
            color_text(self.text_display, "Step", "red_tag", foreground="red")
            color_text(self.text_display, "Finished", "green_tag", foreground="green")

root = tk.Tk()
app = FractionCalculator(root)
root.mainloop()
