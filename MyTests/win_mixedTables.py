import random
import time
import os, time

def quiz():
    total = 0
    correct = 0

    print("🔥 Times Tables Challenge 🔥")
    print("You have 10 seconds to answer each question.")
    print("Type 'q' to quit\n")

    while True:
        time.sleep(2)
        os.system("clear")
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        answer = a * b

        print(f"{a} × {b} = ?")

        start_time = time.time()
        user_input = input("💨 > ").strip().lower()
        end_time = time.time()

        if user_input in ["q", "quit"]:
            break

        total += 1

        time_taken = end_time - start_time

        try:
            user_answer = int(user_input)

            if time_taken > 10:
                print(f"⏰ Too slow! ({time_taken:.1f}s) Answer = {answer}\n")
            elif user_answer == answer:
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
