import random
import signal
import time, os

def timeout_handler(signum, frame):
    raise TimeoutError

def generate_question():
    if random.choice(["mul", "div"]) == "mul":
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        return f"{a} x {b}", a * b
    else:
        b = random.randint(2, 9)
        result = random.randint(2, 9)
        a = b * result
        return f"{a} ÷ {b}", result

def quiz():
    total = 0
    correct = 0

    print("Mixed Times Tables Quiz (2–9)")
    print("You have 10 seconds per question. Type 'q' to exit.\n")

    signal.signal(signal.SIGALRM, timeout_handler)

    while True:
        time.sleep(2)
        os.system("clear")
        question, answer = generate_question()

        try:
            signal.alarm(10)  # start 10-second timer
            user_input = input(f"{question} = ")
            signal.alarm(0)  # cancel timer

            if user_input.lower() == "q":
                break

            total += 1

            if int(user_input) == answer:
                print("✅ Correct!\n")
                correct += 1
            else:
                print(f"❌ Wrong! Answer = {answer}\n")

        except TimeoutError:
            total += 1
            print(f"\n⏰ Time's up! Answer = {answer}\n")

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
