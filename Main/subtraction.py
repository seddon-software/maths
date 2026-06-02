import random
import os, time

def generate_question():
    number1 = random.randint(100, 999)/1000
    number2 = random.randint(100, 999)/1000
    if number1 > number2:
        question = f"What is {number1} - {number2}?"
        answer = number1 - number2
    else:
        question = f"What is {number2} - {number1}?"
        answer = number2 - number1
    return question, round(answer, 2)

def quiz():
    total = 0
    correct = 0
    print("💯 Percentages Quiz 💯")
    print("Answer as a number (decimals allowed)")
    print("Type 'q' to quit\n")

    while True:
        finish = input("?")
        if finish == "q": break
        os.system("clear")
        question, answer = generate_question()

        user_input = input(f"{question}\n💨 > ").strip().lower()


        total += 1

        try:
            user_answer = float(user_input)

            if abs(user_answer - answer) < 0.01:
                print("🔥 Correct!\n")
                correct += 1
            else:
                print(f"❌ Incorrect! Answer = {answer}\n")

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
