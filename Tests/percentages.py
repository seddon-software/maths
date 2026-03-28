import random
import os, time

def generate_question():
    question_type = random.choice(["percent_of", "increase", "decrease"])

    if question_type == "percent_of":
        percent = random.choice([5, 10, 20, 25, 50, 75])
        number = random.randint(10, 200)
        answer = number * percent / 100
        question = f"What is {percent}% of {number}?"

    elif question_type == "increase":
        percent = random.choice([10, 20, 25, 50])
        number = random.randint(10, 200)
        answer = number * (1 + percent / 100)
        question = f"Increase {number} by {percent}%"

    else:  # decrease
        percent = random.choice([10, 20, 25, 50])
        number = random.randint(10, 200)
        answer = number * (1 - percent / 100)
        question = f"Decrease {number} by {percent}%"

    return question, round(answer, 2)

def quiz():
    total = 0
    correct = 0

    print("💯 Percentages Quiz 💯")
    print("Answer as a number (decimals allowed)")
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
