
import random
import os

QUESTIONS = 20

# Conversion name, starting unit, target unit,
# conversion function and conversion information

CONVERSIONS = [
    ("cm to inches", "cm", "inches",
     lambda x: x / 2.54,
     "1 inch = 2.54 cm"),

    ("inches to cm", "inches", "cm",
     lambda x: x * 2.54,
     "1 inch = 2.54 cm"),

    ("km to miles", "km", "miles",
     lambda x: x / 1.609344,
     "1 mile = 1.609344 km"),

    ("miles to km", "miles", "km",
     lambda x: x * 1.609344,
     "1 mile = 1.609344 km"),

    ("metres to feet", "metres", "feet",
     lambda x: x / 0.3048,
     "1 foot = 0.3048 metres"),

    ("feet to metres", "feet", "metres",
     lambda x: x * 0.3048,
     "1 foot = 0.3048 metres"),

    ("kg to pounds", "kg", "pounds",
     lambda x: x / 0.45359237,
     "1 kg = 2.20462 pounds"),

    ("pounds to kg", "pounds", "kg",
     lambda x: x * 0.45359237,
     "1 kg = 2.20462 pounds"),

    ("litres to UK pints", "litres", "pints",
     lambda x: x / 0.56826125,
     "1 UK pint = 0.56826125 litres"),

    ("UK pints to litres", "pints", "litres",
     lambda x: x * 0.56826125,
     "1 UK pint = 0.56826125 litres"),

    ("Celsius to Fahrenheit", "°C", "°F",
     lambda x: x * 1.8 + 32,
     "°F = (°C × 1.8) + 32"),

    ("Fahrenheit to Celsius", "°F", "°C",
     lambda x: (x - 32) / 1.8,
     "°C = (°F - 32) ÷ 1.8"),
]


def clear_screen():
    os.system("clear")


def generate_question(count):

    name, from_unit, to_unit, convert, factor = (
        random.choice(CONVERSIONS)
    )

    # Generate starting value
    if from_unit in ("°C", "°F"):
        value = random.randint(-10, 40)
    else:
        value = random.randint(1, 100)

    answer = round(convert(value), 2)

    question = f"{count}: Convert {value} {from_unit} into {to_unit}"

    return question, answer, to_unit, factor


def quiz():

    correct = 0
    total = 0

    clear_screen()

    print("CONVERSIONS QUIZ")
    print("----------------")
    print(f"{QUESTIONS} questions")
    print("Answers should be given to 2 decimal places.")
    print("Type 'q' to exit.\n")

    input("Press ENTER to start...")

    for count in range(1, QUESTIONS + 1):

        clear_screen()

        question, answer, unit, factor = generate_question(count)

        print("CONVERSIONS QUIZ")
        print("----------------\n")

        print(f"\033[91m{question}\033[0m")
        print(f"\nConversion information: {factor}")

        user_input = input("\nYour answer: ").strip()

        if user_input.lower() == "q":
            break

        try:
            user_answer = float(user_input)

        except ValueError:
            print("\nPlease enter a valid number.")
            input("\nPress ENTER to continue...")
            continue

        total += 1

        if round(user_answer, 2) == answer:
            print("\nCorrect!")
            correct += 1
        else:
            print(f"\nWrong! Answer = {answer:.2f} {unit}")

        input("\nPress ENTER for next question...")

    clear_screen()

    print("FINAL RESULTS")
    print("-------------")

    print(f"Questions answered: {total}")
    print(f"Correct: {correct}")

    if total > 0:
        accuracy = correct / total * 100
        print(f"Accuracy: {accuracy:.1f}%")
    else:
        print("No questions answered.")

    print("\nQuiz finished!")


if __name__ == "__main__":
    quiz()
