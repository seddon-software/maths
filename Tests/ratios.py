import random
import time
import os
import platform

IS_WINDOWS = platform.system() == "Windows"

# Only use signal on non-Windows systems
if not IS_WINDOWS:
    import signal

    def timeout_handler(signum, frame):
        raise TimeoutError

    signal.signal(signal.SIGALRM, timeout_handler)

def clear_screen():
    os.system("cls" if IS_WINDOWS else "clear")

names = ["Alex", "Sam", "Jordan", "Taylor", "Chris"]
items = ["sweets", "stickers", "coins", "marbles", "football cards"]

def generate_question():
    name1, name2 = random.sample(names, 2)
    item = random.choice(items)

    a = random.randint(1, 5)
    b = random.randint(1, 5)
    factor = random.randint(2, 10)

    if random.choice([True, False]):
        given = a * factor
        answer = b * factor
        question = (
            f"{name1} and {name2} share {item} in the ratio {a}:{b}.\n"
            f"{name1} has {given} {item}.\n"
            f"How many does {name2} have?"
        )
    else:
        given = b * factor
        answer = a * factor
        question = (
            f"{name1} and {name2} share {item} in the ratio {a}:{b}.\n"
            f"{name2} has {given} {item}.\n"
            f"How many does {name1} have?"
        )

    return question, answer

def quiz():
    total = 0
    correct = 0

    print("🔥 Real-Life Ratio Challenge 🔥")
    print("You have 20 seconds to answer.")
    print("Press 'q' then Enter to quit.\n")

    while True:
        time.sleep(2)
        clear_screen()
        question, answer = generate_question()

        print("⏱️ Go!\n")

        try:
            if IS_WINDOWS:
                # Windows: measure time
                start = time.time()
                user_input = input(f"{question}\n💨 > ")
                elapsed = time.time() - start

                if user_input.lower() == "q":
                    break

                total += 1

                if elapsed > 20:
                    print(f"\n⏰ Too slow! ({elapsed:.1f}s) Answer = {answer}\n")
                    continue

            else:
                # Linux/macOS: real timeout
                signal.alarm(20)
                user_input = input(f"{question}\n💨 > ")
                signal.alarm(0)

                if user_input.lower() == "q":
                    break

                total += 1

        except TimeoutError:
            total += 1
            print(f"\n⏰ Time’s up! Answer = {answer}\n")
            continue

        # Check answer
        try:
            if int(user_input) == answer:
                print("🔥 Correct!\n")
                correct += 1
            else:
                print(f"❌ Not quite! Answer = {answer}\n")
        except ValueError:
            print("⚠️ Numbers only!\n")

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
    