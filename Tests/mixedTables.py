import random
import time
import os
import platform

IS_WINDOWS = platform.system() == "Windows"

# Only import signal on non-Windows systems
if not IS_WINDOWS:
    import signal

    def timeout_handler(signum, frame):
        raise TimeoutError

    signal.signal(signal.SIGALRM, timeout_handler)

def clear_screen():
    os.system("cls" if IS_WINDOWS else "clear")

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

    while True:
        time.sleep(2)
        clear_screen()
        question, answer = generate_question()

        try:
            if IS_WINDOWS:
                # Windows: measure time
                start = time.time()
                user_input = input(f"{question} = ")
                elapsed = time.time() - start

                if user_input.lower() == "q":
                    break

                total += 1

                if elapsed > 10:
                    print(f"\n⏰ Too slow! ({elapsed:.1f}s) Answer = {answer}\n")
                    continue

            else:
                # Linux/macOS: real timeout
                signal.alarm(10)
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