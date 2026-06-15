import random
import signal
import time
import os
import platform


TIMEOUT = 20

def timeout_handler(signum, frame):
    raise TimeoutError

signal.signal(signal.SIGALRM, timeout_handler)

def clear_screen():
    os.system("clear")

def generate_question(count):
    if random.choices(["mul", "div"], weights=[1, 1])[0] == "mul":
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        result = a * b
        return f"{count}:  {a} x {b}", result
    else:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        result = a * b
        return f"{count}:  {result} ÷ {a}", b

def quiz():
    count = 0
    total = 0
    correct = 0
    os.system("clear")
    print("Mixed Times Tables Quiz")
    print(f"You have {TIMEOUT} seconds per question. Type 'q' to exit.\n")
    time.sleep(TIMEOUT)
    while count < 20:
        count += 1
        time.sleep(2)
        clear_screen()
        question, answer = generate_question(count)

        try:
            signal.alarm(TIMEOUT)
            user_input = input(f"{question} = ")
            signal.alarm(0)

            if user_input.lower() == "q":
                break

            total += 1
        except TimeoutError:
            total += 1
            print(f"\n⏰ Time's up! Answer = {answer}\n")
            continue

        except ValueError:
            print("⚠️ Please enter a number.\n")
            continue

        # Check answer
        try:
            if int(user_input) == answer:
                print("✅ Correct!\n")
                correct += 1
            else:
                print(f"❌ Wrong! Answer = {answer}\n")
        except ValueError:
            print("⚠️ Please enter a number.\n")

    if total > 0:
        accuracy = (correct / total) * 100
        print("\n📊 Final Stats")
        print(f"Total: {total}")
        print(f"Correct: {correct}")
        print(f"Accuracy: {accuracy:.1f}%")
    else:
        print("No questions answered.")

if __name__ == "__main__":
    quiz()