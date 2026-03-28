import random
import os, time

def generate_question():
    question_type = random.choice(["area", "perimeter", "missing_side"])

    length = random.randint(2, 20)
    width = random.randint(2, 20)

    if question_type == "area":
        answer = length * width
        question = f"A rectangle has length {length} and width {width}. What is its area?"

    elif question_type == "perimeter":
        answer = 2 * (length + width)
        question = f"A rectangle has length {length} and width {width}. What is its perimeter?"

    else:  # missing side
        area = length * width
        question = f"A rectangle has area {area} and width {width}. What is its length?"
        answer = length

    return question, answer

def quiz():
    total = 0
    correct = 0

    print("📐 Rectangle Quiz 📐")
    print("Area = length × width")
    print("Perimeter = 2 × (length + width)")
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