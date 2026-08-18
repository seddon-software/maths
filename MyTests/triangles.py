import random
import os, time

def generate_question():
    question_type = random.choice(["area", "perimeter", "missing_side"])

    base = random.randint(2, 20)
    height = random.randint(2, 20)

    side1 = random.randint(2, 20)
    side2 = random.randint(2, 20)
    side3 = random.randint(2, 20)

    if question_type == "area":
        area = 0.5 * base * height
        question = f"A triangle has base {base} and height {height}. What is its area?"
        answer = area

    elif question_type == "perimeter":
        question = f"A triangle has sides {side1}, {side2}, and {side3}. What is its perimeter?"
        answer = side1 + side2 + side3

    else:  # missing side
        total = side1 + side2 + side3
        question = f"A triangle has perimeter {total}. Two sides are {side1} and {side2}. What is the third side?"
        answer = side3

    return question, answer

def quiz():
    total = 0
    correct = 0

    print("🔺 Triangle Quiz 🔺")
    print("Area = 1/2 × base × height")
    print("Perimeter = sum of all sides")
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
