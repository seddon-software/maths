import random
import math
import os, time

def generate_question():
    shape_type = random.choice(["circle", "semicircle", "quadrant"])

    if random.choice([True, False]):
        r = random.randint(1, 10)
        radius = r
        given = f"radius {r}"
    else:
        d = random.randint(2, 20)
        radius = d / 2
        given = f"diameter {d}"

    full_area = math.pi * radius * radius

    if shape_type == "circle":
        area = full_area
        shape_name = "circle"
    elif shape_type == "semicircle":
        area = full_area / 2
        shape_name = "semicircle"
    else:
        area = full_area / 4
        shape_name = "quadrant"

    question = (
        f"A {shape_name} has {given}.\n"
        f"What is its area? (round to 2 decimal places)"
    )

    return question, round(area, 2)

def quiz():
    total = 0
    correct = 0

    print("🔵 Circle Area Challenge 🔵")
    print("Includes circles, semicircles, and quadrants")
    print("Use A = πr² (and fractions of it)")
    print("Round to 2 decimal places.")
    print("Type 'q' anytime to quit.\n")

    while True:
        time.sleep(2)
        os.system("clear")
        question, answer = generate_question()

        user_input = input(f"{question}\n💨 > ").strip().lower()

        if user_input in ["q", "quit"]:
            break

        total += 1

        try:
            user_answer = float(user_input)
            if abs(user_answer - answer) < 0.01:
                print("🔥 Correct!\n")
                correct += 1
            else:
                print(f"❌ Not quite! Answer = {answer}\n")
        except ValueError:
            print("⚠️ Enter a number or 'q' to quit.\n")

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
