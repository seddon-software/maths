import random
import math
import os, time

def generate_question():
    while True:
        a = random.randint(2, 50)
        b = random.randint(2, 50)

        hcf = math.gcd(a, b)

        if hcf != 1:  # exclude cases where answer is 1
            question = f"What is the highest common factor of {a} and {b}?"
            return question, hcf

def quiz():
    total = 0
    correct = 0

    print("🧠 Highest Common Factor Quiz 🧠")
    print("No questions will have an answer of 1.")
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
