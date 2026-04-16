import tkinter as tk
import math
from fractions import Fraction
import random


Josh = True


primes = [2, 3, 5, 7, 11]


def to_mixed(n, d):
    f = Fraction(n, d)
    whole = f.numerator // f.denominator
    remainder = abs(f.numerator % f.denominator)
    if remainder == 0:
        return ""
    return f"{whole} {str(Fraction(remainder, f.denominator))}"

def getNumber():
    number = ""
    while number == "":
        a1 = random.choice([i for i in range(20) if i%2 == 1])
        a2 = random.choice(primes)
        number = f"{to_mixed(a1,a2)}"
    return number

def stages():
    try:
        number1 = getNumber()
        number2 = getNumber()
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
    except Exception as e:
        print(f"stages: {e}")

g = stages()
content = ""
n = 1.0
finished = False

def show_next_stage():
    global content, n, g, finished
    if finished: root.quit()
    try:
        c = next(g)
        content += c
        if c == "FINISHED": 
            finished = True
        text.delete(n, tk.END)
        text.insert(n, content)
    except Exception as e:
        if not finished:
            print(f"show_next_stage: {content} {finished} {n} {e}", end="")
    return

root = tk.Tk()
root.title("Fraction Calculator")
root.geometry("800x900")

text = tk.Text(root, width=60, height=30, font=("Courier", 16, "bold"))
text.pack(pady=10)

button = tk.Button(root, text="Next Stage", command=show_next_stage, font=("Arial", 16))
button.pack()
        
root.mainloop()
