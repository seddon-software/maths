import random
import time
import os
import platform

IS_WINDOWS = platform.system() == "Windows"
TIMEOUT = 20

# Only import signal on non-Windows systems
if not IS_WINDOWS:
    import signal

    def timeout_handler(signum, frame):
        raise TimeoutError

    signal.signal(signal.SIGALRM, timeout_handler)

def clear_screen():
    os.system("cls" if IS_WINDOWS else "clear")

def generate_question():
    if random.choices(["mul", "div"], weights=[1, 1])[0] == "mul":
        a = random.randint(6, 9)
        b = random.randint(6, 9)
        result = a * b
        return f"{a} x {b}", result
    else:
        a = random.randint(6, 9)
        b = random.randint(6, 9)
        result = a * b
        return f"{result} ÷ {a}", b

def quiz():
    total = 0
    correct = 0
    os.system("clear")
    print("Mixed Times Tables Quiz")
    print(f"You have {TIMEOUT} seconds per question. Type 'q' to exit.\n")
    time.sleep(TIMEOUT)
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

                if elapsed > TIMEOUT:
                    print(f"\n⏰ Too slow! ({elapsed:.1f}s) Answer = {answer}\n")
                    continue

            else:
                # Linux/macOS: real timeout
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