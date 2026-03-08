import tkinter as tk
import math
from fractions import Fraction


Josh = True

def stages():
    # whole + fraction
    number1 = "5 3/4"
    number2 = "2 5/8"

    n1 = number1.split(' ')
    n2 = number2.split(' ')
    f1_w = Fraction(n1[0])
    f1_n = Fraction(n1[1]).numerator
    f1_d = Fraction(n1[1]).denominator
    f2_w = Fraction(n2[0])
    f2_n = Fraction(n2[1]).numerator
    f2_d = Fraction(n2[1]).denominator
    d = math.lcm(f1_d, f2_d)
    f1n = int(f1_n*d/f1_d)
    f2n = int(f2_n*d/f2_d)
    f1 = Fraction(f1n, d, _normalize=False)
    f2 = Fraction(f2n, d, _normalize=False)
    fraction = Fraction(f1.numerator - f2.numerator, d)
    whole = f1_w - f2_w
    text.delete(1.0, tk.END)

    contents = [
        [0, f"Subtract the numbers\n"],
        [1, f"{number1} - {number2}\n\n"],
        [3, ""],
        [0, f"Start by subtracting the fractions\n"],
        [1, f"{n1[1]} - {n2[1]}\n\n"],
        [3, ""],
        [0, f"Find the LCD (Least Common Denominator)\n"],
        [3, ""],
        [2, f"LCD of {f1_d} and {f2_d} = ???\n"],
        [3, ""],
        [0, f"LCD of {f1_d} and {f2_d} = {d}\n\n"],
        [3, ""],
        [0, f"Convert to equivalent fractions\n"],
        [3, ""],
        [2, f"{n1[1]} = ???/{d}\n"],
        [3, ""],
        [1, f"{n1[1]} = {f1}\n"],
        [3, ""],
        [2, f"{n2[1]} = ???/{d}\n"],
        [3, ""],
        [1, f"{n2[1]} = {f2}\n\n"],
        [3, ""],
        [1, f"Subtract the numerators\n"],
        [3, ""],
        [2, f"{f1} - {f2} = ???/{d}\n"],
        [3, ""],
        [1, f"{f1} - {f2} = {fraction}\n\n"],
        [3, ""],
        [0, f"Subtract the whole numbers\n"],
        [1, f"{f1_w} - {f2_w} = ???\n"],
        [3, ""],
        [0, f"{f1_w} - {f2_w} = {whole}\n\n"],
        [3, ""],
        [0, f"Combine the whole numbers with the fraction\n"],
        [1, f"{number1} - {number2} = ???\n"],
        [3, ""],
        [0, f"{number1} - {number2} = {whole} {fraction}\n\n"],
        [3, ""],
        [0, "FINISHED"],
        [3, ""],
    ]
    for i, c in contents:
        if i == 0: content = c
        elif i == 1: content += c
        elif i == 2 and (Josh): content = ""; yield c 
        elif i == 3: yield content; content = ""
        else: pass
    return
    # if fraction > 1:
    #     whole = int(fraction)
    #     fraction = fraction - whole
    #     content += f"Reduce fraction\n"

    # if fraction > 1:
    #     if(Josh): content = f"{fraction} = {whole} + ???/{d}\n\n"
    #     yield content



g = stages()

content = ""
n = 1.0
def show_next_stage():
    global content, n
    try:
        content += next(g)
        text.delete(1.0, tk.END)
        text.insert(n, content)
    except:
        pass

root = tk.Tk()
root.title("Fraction Calculator")
root.geometry("800x900")

text = tk.Text(root, width=60, height=30, font=("Courier", 16, "bold"))
text.pack(pady=10)

button = tk.Button(root, text="Next Stage", command=show_next_stage, font=("Arial", 16))
button.pack()
        
root.mainloop()
