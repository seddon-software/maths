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

class Pair:
    class Number:
        def __init__(self, f):
            self.f = f
            self.numerator = Fraction(f).numerator
            self.denominator = Fraction(f).denominator
        def get_new_numerator(self, other):
            self.new_numerator = self.numerator * other.denominator 
            return self.new_numerator 
        def getValue(self):
            return self.f
    def __init__(self, f1, f2):
        n1 = Pair.Number(f1)
        n2 = Pair.Number(f2)
        self.common_denominator = n1.denominator * n2.denominator
        self.denominators = [n1.denominator, n2.denominator]
        self.numerators = [n1.numerator, n2.numerator]
        self.new_numerators = [n1.get_new_numerator(n2), n2.get_new_numerator(n1)]
        self.values = [n1.getValue(),n2.getValue()]

class Stages():
    def __init__(self, root, f1, f2):
        self.root = root
        self.root.title("Fraction Addition Calculator")
        self.root.geometry("800x800")
        
        self.stage = 0
        self.pair = Pair(f1, f2)

        self.text_display = tk.Text(root, width=60, height=30, font=("Courier", 16, "bold"))
        self.text_display.pack(pady=10)
        
        self.button = tk.Button(root, text="Next Stage", command=self.show_next_stage, font=("Arial", 16))
        self.button.pack()
        
        self.show_stage()
    
    def show_stage(self):
        self.text_display.delete(1.0, tk.END)
        content = ""
        
        if self.stage >= 0:
            content += f"\nStep 1: Add the fractions\n"
            content += f"{self.pair.values[0]} + {self.pair.values[1]}\n"
        
        if self.stage >= 1:
            content += f"\nStep 2: Find the new denominator\n"
            d = self.pair.common_denominator

        if self.stage >= 2:
            content += f"denominator = {d}\n"

        if self.stage >= 3:
            content += f"\nStep 3: Convert to equivalent fractions\n"
            p = self.pair
            content += f"{p.numerators[0]}/{p.denominators[0]} = ???/{d}\n"
        if self.stage >= 4:
            content += f"{p.numerators[0]}/{p.denominators[0]} = {self.pair.new_numerators[0]}/{d}\n"
        if self.stage >= 5:
            content += f"{p.numerators[1]}/{p.denominators[1]} = ???/{d}\n"
        if self.stage >= 6:
            content += f"{p.numerators[1]}/{p.denominators[1]} = {self.pair.new_numerators[1]}/{d}\n"
        
        if self.stage >= 7:
            content += f"\nStep 4: Add the numerators\n"
            content += f"{p.new_numerators[0]}/{d} + {p.new_numerators[1]}/{d} = ???/{d}\n"
            numerator = p.new_numerators[0] + p.new_numerators[1]

        if self.stage >= 8:
            result = f"{numerator}/{d}"
            content += f"{p.new_numerators[0]}/{d} + {p.new_numerators[1]}/{d} = {numerator}/{d}\n"
        if self.stage >= 9:
                content += f"\nStep 5: Reduce fraction\n"
                denominator = d
                g = gcd(numerator, denominator)

                reduced_numerator = numerator//g
                reduced_denominator = denominator//g

                reducedFraction = f"{reduced_numerator}/{reduced_denominator}"
                content += f"{numerator}/{d} = ???\n"
        if self.stage >= 10:
                content += f"{numerator}/{d} = ???/{reduced_denominator}\n"
        if self.stage >= 11:
                content += f"{numerator}/{d} = {reducedFraction}\n"

        if self.stage >= 12:
            if reduced_numerator > reduced_denominator:
                content += f"\nStep 6: Normalise fraction\n"
                content += f"{reducedFraction} = 1 + ???/{reduced_denominator}\n"
            else:
                self.stage += 1
                content += f"\n"
        if self.stage >= 13:
            if reduced_numerator > reduced_denominator:
                content += f"{reducedFraction} = 1 + {reduced_numerator - reduced_denominator}/{reduced_denominator}\n"
            content += f"\nFinished\n"
    
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
app = Stages(root, "5/8", "3/7")
root.mainloop()

