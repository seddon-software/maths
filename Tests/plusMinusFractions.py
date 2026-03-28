import random
from fractions import Fraction
import os, time

def generate_question():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    d = random.randint(1, 9)

    f1 = Fraction(a, b)
    f2 = Fraction(c, d)

    op = random.choice(["+", "-"])

    if op == "+":
        result = f1 + f2
    else:
        result = f1 - f2

    question = f"{f1} {op} {f2} = ?"
    return question, result

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

def quiz():
    total = 0
    correct = 0

    print("🧠 Fractions Challenge 🧠")
    print("Answers can be mixed numbers (e.g. 1 2/3)")
    print("Type 'q' to quit\n")

    while True:
        time.sleep(2)
        os.system("clear")
        question, answer = generate_question()

        user_input = input(f"{question}\n💨 > ").strip().lower()

        if user_input in ["q", "quit"]:
            break

        total += 1

        user_fraction = parse_fraction(user_input)

        if user_fraction is None:
            print("⚠️ Enter like 3/4 or 1 2/3\n")
            continue

        if user_fraction == answer:
            print("🔥 Correct!\n")
            correct += 1
        else:
            print(f"❌ Not quite! Answer = {to_mixed(answer)}\n")

    if total > 0:
        accuracy = (correct / total) * 100
        print("\n🏁 Final Results")
        print(f"📊 Total: {total}")
        print(f"✅ Correct: {correct}")
        print(f"🎯 Accuracy: {accuracy:.1f}%")
    else:
        print("\nNo questions answered.")

if __name__ == "__main__":
    quiz()
    