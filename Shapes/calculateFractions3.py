import tkinter as tk
import math
from fractions import Fraction


Josh = True

def stages():
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
    text.delete(1.0, tk.END)

    content = f"Subtract the numbers\n"
    content += f"{number1} - {number2}\n\n"
    yield content
    content = f"Start by subtracting the fractions\n"
    content += f"{n1[1]} - {n2[1]}\n\n"
    yield content
    content = f"Find the LCD (Least Common Denominator)\n"
    if(Josh): 
        content += f"LCD of {f1_d} and {f2_d} = ???\n"
        yield content

    content = f"LCD of {f1_d} and {f2_d} = {d}\n\n"
    yield content
    content = f"Convert to equivalent fractions\n"
    yield content
    f1n = int(f1_n*d/f1_d)
    f2n = int(f2_n*d/f2_d)
    f1 = Fraction(f1n, d, _normalize=False)
    f2 = Fraction(f2n, d, _normalize=False)
    if(Josh): 
        content = f"{n1[1]} = ???/{d}\n"
        yield content
    content = f"{n1[1]} = {f1}\n"
    yield content
    if(Josh): 
        content = f"{n2[1]} = ???/{d}\n"
        yield content
    content = f"{n2[1]} = {f2}\n\n"
    yield content

    content = f"Subtract the numerators\n"
    fraction = Fraction(f1.numerator - f2.numerator, d)
    yield content

    if(Josh): 
        content = f"{f1} - {f2} = ???/{d}\n"
        yield content
    content = f"{f1} + {f2} = {fraction}\n\n"
    yield content

    if fraction > 1:
        whole = int(fraction)
        fraction = fraction - whole
        content += f"Reduce fraction\n"

    if fraction > 1:
        if(Josh): content = f"{fraction} = {whole} + ???/{d}\n\n"
        yield content

    content = f"Subtract the whole numbers\n"
    content += f"{f1_w} - {f2_w} = ???\n"
    yield content
    whole = f1_w - f2_w
    content = f"{f1_w} - {f2_w} = {whole}\n\n"
    yield content

    content = f"Combine the whole numbers with the fraction\n"
    content += f"{number1} - {number2} = ???\n"
    yield content

    content = f"{number1} - {number2} = {whole} {fraction}\n\n"
    yield content

    content = "FINISHED"
    yield content

    return

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
