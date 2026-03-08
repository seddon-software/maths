
f1 = "5 3/4"
f2 = "2 5/8"
op = "-"

import tkinter as tk
import math
from fractions import Fraction

Josh = True
#Josh = False

class FractionCalculator:
    def __init__(self, root):
        def split(f):
            f.replace(' ', '+')
            return f
        self.root = root
        self.root.title("Fraction Calculator")
        self.root.geometry("800x600")
        
        self.stage = 0
        self.n1 = f1
        self.n2 = f2
        self.f1 = f1.split(' ')
        self.f2 = f2.split(' ')
        self.f1_w = Fraction(self.f1[0])
        self.f1_n = Fraction(self.f1[1]).numerator
        self.f1_d = Fraction(self.f1[1]).denominator
        self.f2_w = Fraction(self.f2[0])
        self.f2_n = Fraction(self.f2[1]).numerator
        self.f2_d = Fraction(self.f2[1]).denominator
        self.d = math.lcm(self.f1_d, self.f2_d)

        self.text_display = tk.Text(root, width=60, font=("Courier", 16, "bold"))
        self.text_display.pack(pady=10)
        
        self.button = tk.Button(root, text="Next Stage", command=self.show_next_stage, font=("Arial", 16))
        self.button.pack()
        
#        self.show_stage()
    
    def show_next_stage(self):
        def stages():
            global f1, f2

            self.text_display.delete(1.0, tk.END)
            content = f"Step 1: Subtract the numbers\n"
            content += f"{f1} - {f2}\n\n"
            yield content

            content = f"Step 1: Subtract the fractions\n"
            content += f"{self.f1[1]} - {self.f2[1]}\n\n"
            yield content
            
            content = f"Step 2: Find the LCD (Least Common Denominator)\n"
            if(Josh): content = f"LCD of {self.f1_d} and {self.f2_d} = ???\n"
            yield content

            content = f"LCD of {self.f1_d} and {self.f2_d} = {self.d}\n\n"
            content += f"Step 3: Convert to equivalent fractions\n"
            yield content
            f1n = int(self.f1_n*self.d/self.f1_d)
            f2n = int(self.f2_n*self.d/self.f2_d)
            f1 = Fraction(f1n, self.d, _normalize=False)
            f2 = Fraction(f2n, self.d, _normalize=False)
            if(Josh): content = f"{self.f1[1]} = ???/{self.d}\n"
            content += f"{self.f1[1]} = {f1}\n"
            yield content
            if(Josh): content += f"{self.f2[1]} = ???/{self.d}\n"
            content += f"{self.f2[1]} = {f2}\n\n"
            
            content += f"Step 4: Subtract the numerators\n"
            result = Fraction(f1.numerator - f2.numerator, self.d)

            if(Josh): content += f"{f1} - {f2} = ???/{self.d}\n"
            content += f"{f1} + {f2} = {result}\n\n"
            
            if result > 1:
                content += f"{result} = {whole} {fraction}\n\n"


            content += f"Step 0: Subtract the whole numbers\n"
            content += f"{self.f1_w} {op} {self.f2_w} = ???\n"

            content += f"{self.f1_w} {op} {self.f2_w} = {self.f1_w - self.f2_w}\n"

            if result > 1:
                whole = int(result)
                fraction = result - whole
                content += f"Step 5: Reduce fraction\n"
            
            if result > 1:
                if(Josh): content += f"{result} = {whole} + ???/{self.d}\n"

            content += f"Finished\n"
            yield content      
            # self.text_display.insert(1.0, content)
            # self.text_display.config(state=tk.DISABLED)

        g = stages()

        content = ""
        while True:
            content += next(g)
            self.text_display.insert(1.0, content)
            self.text_display.config(state=tk.NORMAL)
        #    self.text_display.config(state=tk.DISABLED)
        # if self.stage < 14:
        #     self.stage += 1
        #     self.text_display.config(state=tk.NORMAL)
        #     self.show_stage()

root = tk.Tk()
app = FractionCalculator(root)
root.mainloop()
