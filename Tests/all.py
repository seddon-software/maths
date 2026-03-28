import random
import math
import os, time
from fractions import Fraction

def to_mixed(frac):
    whole = frac.numerator // frac.denominator
    remainder = frac.numerator % frac.denominator

    if remainder == 0:
        return str(whole)
    elif whole == 0:
        return f"{remainder}/{frac.denominator}"
    else:
        return f"{whole} {remainder}/{frac.denominator}"

def parse_fraction(user_input):
    try:
        if " " in user_input:
            whole, frac = user_input.split()
            num, den = frac.split("/")
            return Fraction(int(whole)) + Fraction(int(num), int(den))
        elif "/" in user_input:
            num, den = user_input.split("/")
            return Fraction(int(num), int(den))
        else:
            return Fraction(int(user_input), 1)
    except:
        return None

def generate_question():
    q_type = random.choice([
        "times", "fraction", "percent", "hcf", "lcd", "rectangle", "triangle", "circle"
    ])

    # TIMES TABLES
    if q_type == "times":
        a, b = random.randint(2, 9), random.randint(2, 9)
        return f"{a} × {b} = ?", a * b, "number"

    # FRACTIONS
    elif q_type == "fraction":
        f1 = Fraction(random.randint(1,9), random.randint(1,9))
        f2 = Fraction(random.randint(1,9), random.randint(1,9))
        op = random.choice(["+", "-", "*", "/"])
        result = eval(f"f1 {op} f2")
        return f"{f1} {op} {f2} = ? (a/b or mixed)", result, "fraction"

    # PERCENTAGES
    elif q_type == "percent":
        percent = random.choice([10, 20, 25, 50])
        number = random.randint(10, 200)
        answer = number * percent / 100
        return f"What is {percent}% of {number}?", answer, "number"

    # HCF
    elif q_type == "hcf":
        while True:
            a, b = random.randint(2,50), random.randint(2,50)
            h = math.gcd(a, b)
            if h != 1:
                return f"HCF of {a} and {b}?", h, "number"

    # LCD
    elif q_type == "lcd":
        a, b = random.randint(2,12), random.randint(2,12)
        lcd = abs(a*b)//math.gcd(a,b)
        return f"LCD of {a} and {b}?", lcd, "number"

    # RECTANGLE
    elif q_type == "rectangle":
        l, w = random.randint(2,20), random.randint(2,20)
        if random.choice([True, False]):
            return f"Rectangle length {l}, width {w}. Area?", l*w, "number"
        else:
            return f"Rectangle length {l}, width {w}. Perimeter?", 2*(l+w), "number"

    # TRIANGLE
    elif q_type == "triangle":
        base, height = random.randint(2,20), random.randint(2,20)
        return f"Triangle base {base}, height {height}. Area?", 0.5*base*height, "number"

    # CIRCLE
    else:
        r = random.randint(1,10)
        return f"Circle radius {r}. Area? (2dp)", round(math.pi*r*r,2), "float"

def quiz():
    total = 0
    correct = 0

    print("🔥 Ultimate Maths Quiz 🔥")
    print("Mixed topics — answer carefully!")
    print("Type 'q' to quit\n")

    while True:
        time.sleep(2)
        os.system("clear")

        q, answer, qtype = generate_question()

        user_input = input(f"{q}\n💨 > ").strip().lower()

        if user_input in ["q", "quit"]:
            break

        total += 1

        try:
            if qtype == "fraction":
                user_val = parse_fraction(user_input)
                if user_val == answer:
                    print("🔥 Correct!\n")
                    correct += 1
                else:
                    print(f"❌ Answer = {to_mixed(answer)}\n")

            elif qtype == "float":
                if abs(float(user_input) - answer) < 0.01:
                    print("🔥 Correct!\n")
                    correct += 1
                else:
                    print(f"❌ Answer = {answer}\n")

            else:
                if abs(float(user_input) - answer) < 0.01:
                    print("🔥 Correct!\n")
                    correct += 1
                else:
                    print(f"❌ Answer = {answer}\n")

        except:
            print("⚠️ Invalid input\n")

    if total > 0:
        print("\n🏁 Final Results")
        print(f"📊 Total: {total}")
        print(f"✅ Correct: {correct}")
        print(f"🎯 Accuracy: {correct/total*100:.1f}%")
    else:
        print("\nNo questions answered.")

if __name__ == "__main__":
    quiz()
