import random
import math
import os, time
math.pi = 3.14

def generate_question():
    shape = random.choice(["circle", "semicircle", "quadrant"])
    question_type = random.choice(["area", "perimeter"])

    # radius or diameter
    if random.choice([True, False]):
        r = random.randint(1, 10)
        radius = r
        given = f"radius {r}"
    else:
        d = random.randint(2, 20)
        radius = d / 2
        given = f"diameter {d}"

    if shape == "circle":
        if question_type == "area":
            answer = math.pi * radius * radius
            question = f"A circle has {given}. What is its area?"
        else:
            answer = 2 * math.pi * radius
            question = f"A circle has {given}. What is its circumference?"

    elif shape == "semicircle":
        if question_type == "area":
            answer = (math.pi * radius * radius) / 2
            question = f"A semicircle has {given}. What is its area?"
        else:
            # curved + diameter
            answer = math.pi * radius + (2 * radius)
            question = f"A semicircle has {given}. What is its perimeter?"

    else:  # quadrant
        if question_type == "area":
            answer = (math.pi * radius * radius) / 4
            question = f"A quadrant has {given}. What is its area?"
        else:
            # quarter arc + 2 radii
            answer = (math.pi * radius / 2) + (2 * radius)
            question = f"A quadrant has {given}. What is its perimeter?"

    return question, round(answer, 2)

def quiz():
    total = 0
    correct = 0

    print("🔵 Circle Geometry Quiz 🔵")
    print("Includes circles, semicircles, and quadrants")
    print("Round answers to 2 decimal places")
    print("Type 'q' to quit\n")

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
            print("⚠️ Enter a number\n")

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
