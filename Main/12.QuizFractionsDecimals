
import random
import os
from fractions import Fraction

QUESTIONS = 20

# Denominators allowed for decimal-to-fraction questions
DENOMINATORS = [2, 3, 4, 5, 6, 7, 8]


def mixed_number(fraction):
    """Convert a Fraction into a mixed-number string."""

    whole = fraction.numerator // fraction.denominator
    remainder = fraction.numerator % fraction.denominator

    if remainder == 0:
        return str(whole)

    if whole == 0:
        return str(fraction)

    return f"{whole} {remainder}/{fraction.denominator}"


def generate_question():

    direction = random.choice(["fraction", "decimal"])

    if direction == "fraction":
        # Fraction to decimal
        denominator = random.randint(2, 100)
        numerator = random.randint(1, denominator - 1)

        fraction = Fraction(numerator, denominator)
        answer = float(fraction)

        question = f"Convert {fraction} to a decimal"
        answer_type = "decimal"

    else:
        # Decimal to fraction
        # Only multiples of 1/2 to 1/8
        denominator = random.choice(DENOMINATORS)
        numerator = random.randint(1, denominator * 10)

        fraction = Fraction(numerator, denominator)
        decimal = float(fraction)

        question = f"Convert {decimal:.2f} to a fraction"
        answer = fraction
        answer_type = "fraction"

    return question, answer, answer_type


def main():

    score = 0
    questions_answered = 0

    os.system("clear")

    print("=" * 45)
    print("       FRACTIONS AND DECIMALS QUIZ")
    print("=" * 45)
    print()
    print("20 questions")
    print("Decimal answers: 2 decimal places")
    print("Fraction answers: simplest form")
    print("Use mixed numbers where appropriate")
    print("Enter q to quit")
    print()

    for number in range(1, QUESTIONS + 1):

        question, answer, answer_type = generate_question()

        print(f"\nQuestion {number} of {QUESTIONS}")
        print(f"\033[91m{question}\033[0m")

        user_input = input("Your answer: ").strip()

        if user_input.lower() == "q":
            break

        questions_answered += 1

        try:
            if answer_type == "decimal":

                user_answer = float(user_input)

                correct = round(user_answer, 2) == round(answer, 2)

                if correct:
                    print("Correct!")
                else:
                    print(f"Incorrect. The answer is {answer:.2f}")

            else:
                # Accept either 33/4 or 8 1/4
                parts = user_input.split()

                if len(parts) == 2:
                    whole = int(parts[0])
                    remainder = Fraction(parts[1])

                    if whole < 0:
                        user_answer = whole - remainder
                    else:
                        user_answer = whole + remainder
                else:
                    user_answer = Fraction(user_input)

                correct = user_answer == answer

                if correct:
                    print("Correct!")
                else:
                    print(f"Incorrect. The answer is {mixed_number(answer)}")

            if correct:
                score += 1

        except (ValueError, ZeroDivisionError):
            print("Invalid answer.")
            print(f"The answer is {mixed_number(answer) if answer_type == 'fraction' else f'{answer:.2f}'}")

    print("\n" + "=" * 45)
    print(f"Your score: {score} out of {questions_answered}")
    print("=" * 45)


if __name__ == "__main__":
    main()
