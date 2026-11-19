
import random
import re
import tkinter as tk
import sympy as sp

# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

WIDTH = 1400
HEIGHT = 650

x = sp.Symbol("x")

BG = "white"
BOX_FILL = "#e8f0fa"
BOX_OUTLINE = "#345678"

FONT = ("Arial", 20)

# --------------------------------------------------
# OPERATIONS
# --------------------------------------------------

def make_operations(start):
    operations = []
    current = start

    for _ in range(2):
        choices = [
            ("+", random.randint(2, 9)),
            ("-", random.randint(2, 9)),
            ("×", random.randint(2, 5))
        ]

        # Include division only when it gives a whole number.
        divisors = [
            n for n in range(2, 10)
            if current % n == 0
        ]

        if divisors:
            choices.append(("÷", random.choice(divisors)))

        operation = random.choice(choices)
        operations.append(operation)

        symbol, number = operation

        if symbol == "+":
            current += number
        elif symbol == "-":
            current -= number
        elif symbol == "×":
            current *= number
        elif symbol == "÷":
            current //= number

    return operations, current


def apply_operations(value, operations):
    for symbol, number in operations:
        if symbol == "+":
            value += number
        elif symbol == "-":
            value -= number
        elif symbol == "×":
            value *= number
        elif symbol == "÷":
            value /= number

    return value


def make_algebra_question():
    operations = [
        (random.choice(["+", "-", "×", "÷"]), random.randint(2, 9))
        for _ in range(2)
    ]

    result = x

    for symbol, number in operations:
        if symbol == "+":
            result += number
        elif symbol == "-":
            result -= number
        elif symbol == "×":
            result *= number
        elif symbol == "÷":
            result /= number

    return {
        "type": "algebra",
        "input": "x",
        "output": "?",
        "operations": operations,
        "answer": sp.simplify(result),
        "instruction": "Find an expression for the output."
    }


# --------------------------------------------------
# QUESTION GENERATION
# --------------------------------------------------

def make_question():

    question_type = random.choices(
        [
            "forward",
            "backward",
            "algebra",
            "reverse_algebra",
            "missing_box"
        ],
        weights=[1, 1, 1, 1, 4],
        k=1
    )[0]

    if question_type == "algebra":
        return make_algebra_question()

    start = random.randint(3, 15)
    operations, result = make_operations(start)

    if question_type == "forward":
        return {
            "type": "forward",
            "input": str(start),
            "output": "?",
            "operations": operations,
            "answer": result,
            "instruction": "Calculate the output."
        }

    if question_type == "backward":
        return {
            "type": "backward",
            "input": "?",
            "output": str(result),
            "operations": operations,
            "answer": start,
            "instruction": "Find the missing input."
        }

    if question_type == "reverse_algebra":
        return {
            "type": "reverse_algebra",
            "input": "x",
            "output": str(result),
            "operations": operations,
            "answer": start,
            "instruction": "Find the value of x."
        }

    # One of the middle boxes is unknown.
    missing = random.randint(0, 1)

    return {
        "type": "missing_box",
        "input": str(start),
        "output": str(result),
        "operations": operations,
        "missing": missing,
        "answer": operations[missing],
        "instruction": "Find the missing operation."
    }


# --------------------------------------------------
# WINDOW
# --------------------------------------------------

root = tk.Tk()
root.title("Number Machines")
root.geometry("1450x850")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg=BG,
    highlightthickness=0
)
canvas.pack(padx=15, pady=10)

question_label = tk.Label(root, font=("Arial", 18))
question_label.pack(pady=5)

answer_frame = tk.Frame(root)
answer_frame.pack(pady=10)

tk.Label(
    answer_frame,
    text="Your answer:",
    font=FONT
).pack(side="left", padx=8)

answer_entry = tk.Entry(
    answer_frame,
    font=FONT,
    width=18
)
answer_entry.pack(side="left", padx=8)

feedback = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold")
)
feedback.pack(pady=8)


# --------------------------------------------------
# DRAWING
# --------------------------------------------------

question = None


def draw_box(cx, cy, text):
    w = 125
    h = 75

    canvas.create_rectangle(
        cx - w / 2,
        cy - h / 2,
        cx + w / 2,
        cy + h / 2,
        fill=BOX_FILL,
        outline=BOX_OUTLINE,
        width=3
    )

    canvas.create_text(
        cx, cy,
        text=text,
        font=FONT
    )


def draw_arrow(x1, y1, x2, y2):
    canvas.create_line(
        x1, y1, x2, y2,
        arrow=tk.LAST,
        width=3
    )


def draw_question():
    canvas.delete("all")

    cy = 300
    positions = [150, 500, 850, 1200]

    draw_box(positions[0], cy, question["input"])

    for i in range(2):
        if question["type"] == "missing_box" and i == question["missing"]:
            label = "?"
        else:
            symbol, number = question["operations"][i]
            label = f"{symbol} {number}"

        draw_box(positions[i + 1], cy, label)

    draw_box(positions[3], cy, question["output"])

    for i in range(3):
        draw_arrow(
            positions[i] + 65,
            cy,
            positions[i + 1] - 65,
            cy
        )

    canvas.create_text(
        WIDTH / 2,
        100,
        text="NUMBER MACHINE",
        font=("Arial", 28, "bold")
    )


# --------------------------------------------------
# CHECK ANSWER
# --------------------------------------------------

def check_answer():
    entered = answer_entry.get().strip()

    if not entered:
        feedback.config(text="Please enter an answer.", fg="red")
        return

    try:
        if question["type"] == "missing_box":
            cleaned = entered.lower().replace("×", "*").replace("÷", "/")
            cleaned = re.sub(r"\s+", "", cleaned)

            match = re.fullmatch(
                r"(multiply|times|add|plus|subtract|minus|divide|over|\*|\+|-|/)(\d+)",
                cleaned
            )

            if not match:
                feedback.config(
                    text="Enter an operation and a number, e.g. × 5",
                    fg="red"
                )
                return

            symbol = match.group(1)

            aliases = {
                "multiply": "×", "times": "×", "*": "×",
                "add": "+", "plus": "+", "+": "+",
                "subtract": "-", "minus": "-", "-": "-",
                "divide": "÷", "over": "÷", "/": "÷"
            }

            student_answer = (aliases[symbol], int(match.group(2)))
            correct = student_answer == question["answer"]

        else:
            student_answer = sp.sympify(entered.replace("^", "**"))
            correct = sp.simplify(
                student_answer - question["answer"]
            ) == 0

        if correct:
            feedback.config(text="Correct!", fg="green")
        else:
            feedback.config(text="Not quite. Try again.", fg="red")

    except Exception:
        feedback.config(text="I couldn't understand that answer.", fg="red")


# --------------------------------------------------
# NEXT QUESTION
# --------------------------------------------------

def new_question():
    global question

    question = make_question()

    draw_question()

    question_label.config(text=question["instruction"])

    answer_entry.delete(0, tk.END)
    feedback.config(text="")

    answer_entry.focus_set()


def background_click(event):
    items = canvas.find_overlapping(
        event.x - 2,
        event.y - 2,
        event.x + 2,
        event.y + 2
    )

    if not items:
        new_question()


# --------------------------------------------------
# BUTTONS AND KEYBOARD
# --------------------------------------------------

tk.Button(
    answer_frame,
    text="Check answer",
    font=("Arial", 15),
    command=check_answer
).pack(side="left", padx=8)

tk.Button(
    answer_frame,
    text="Next question",
    font=("Arial", 15),
    command=new_question
).pack(side="left", padx=8)

answer_entry.bind("<Return>", lambda event: check_answer())
canvas.bind("<Button-1>", background_click)
root.bind("<Escape>", lambda event: root.destroy())

new_question()
root.mainloop()
