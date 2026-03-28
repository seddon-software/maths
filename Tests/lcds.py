import random
import math
import os, time

def generate_question():
    a = random.randint(2, 12)
    b = random.randint(2, 12)

    lcd = abs(a * b) // math.gcd(a, b)

    question = f"What is the least common denominator of {a} and {b}?"
    return question, lcd

def quiz():
    total = 0
    correct = 0

    print("🧠 Least Common Denominator Quiz 🧠")
    print("Find the smallest number both denominators go into.")
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
            user_answer = int(user_input)

            if user_answer == answer:
                print("🔥 Correct!\n")
                correct += 1
            else:
                print(f"❌ Not quite! Answer = {answer}\n")

        except ValueError:
            print("⚠️ Enter a whole number\n")

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
