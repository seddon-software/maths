import random
import re
import tkinter as tk
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)

# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

WIDTH = 1400
HEIGHT = 650

# Single-letter variables. "x" is left out because it means multiply.
VARIABLES = ["a", "b", "m", "n", "p", "t", "y", "z"]
SYMBOLS = {name: sp.Symbol(name) for name in VARIABLES}

BG = "white"
BOX_FILL = "#e8f0fa"
BOX_OUTLINE = "#345678"

FONT = ("Arial", 20)

TRANSFORMS = standard_transformations + (implicit_multiplication_application,)

BOX_W = 125
BOX_H = 75
OUTPUT_W = 240
POSITIONS = [150, 500, 850, 1180]

# For output expressions that parse but don't match yet (e.g. "2y" on the
# way to "2y+6"), wait this many milliseconds after the last keystroke
# before turning red.
WRONG_DELAY = 900

# (entry background, border colour)
COLOURS = {
    "neutral": ("white", BOX_OUTLINE),
    "correct": ("#c8f0c8", "#2e9e44"),
    "wrong": ("#f8c9c9", "#d33333"),
}

# Box indices: 0 = input, 1 = first operation, 2 = second operation, 3 = output
INSTRUCTIONS = {
    0: "Type the missing input.",
    1: "Type the missing operation, e.g. x 5",
    2: "Type the missing operation, e.g. / 3",
    3: "Type an expression for the output.",
}

# --------------------------------------------------
# QUESTION GENERATION
# --------------------------------------------------

def format_expr(expr):
    text = str(sp.expand(expr))
    return text.replace("**", "^").replace("*", "")


def make_question():
    var = SYMBOLS[random.choice(VARIABLES)]

    operations = [
        (random.choice(["+", "-", "x", "/"]), random.randint(2, 9))
        for _ in range(2)
    ]

    result = var

    for symbol, number in operations:
        if symbol == "+":
            result += number
        elif symbol == "-":
            result -= number
        elif symbol == "x":
            result *= number
        elif symbol == "/":
            result /= number

    missing = random.randint(0, 3)

    return {
        "variable": var,
        "operations": operations,
        "result": sp.simplify(result),
        "missing": missing,
        "instruction": INSTRUCTIONS[missing],
    }


# --------------------------------------------------
# WINDOW
# --------------------------------------------------

root = tk.Tk()
root.title("Number Machines")
root.geometry("1450x800")

feedback = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold")
)
feedback.pack(side="bottom", pady=12)

question_label = tk.Label(root, font=("Arial", 18))
question_label.pack(side="bottom", pady=5)

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg=BG,
    highlightthickness=0
)
canvas.pack(side="top", fill="both", expand=True, padx=15, pady=10)

answer_var = tk.StringVar()

# The answer box lives on the canvas, inside whichever box is missing.
answer_entry = tk.Entry(
    canvas,
    textvariable=answer_var,
    font=FONT,
    width=11,
    justify="center",
    relief="flat",
    bg="white",
    highlightthickness=3,
    highlightbackground=BOX_OUTLINE,
    highlightcolor=BOX_OUTLINE
)


# --------------------------------------------------
# DRAWING
# --------------------------------------------------

question = None
pending_job = None


def box_width(index):
    return OUTPUT_W if index == 3 else BOX_W


def draw_box(index, text):
    cx = POSITIONS[index]
    cy = 300
    w = box_width(index)

    canvas.create_rectangle(
        cx - w / 2,
        cy - BOX_H / 2,
        cx + w / 2,
        cy + BOX_H / 2,
        fill=BOX_FILL,
        outline=BOX_OUTLINE,
        width=3
    )

    if text is not None:
        canvas.create_text(cx, cy, text=text, font=FONT)


def draw_arrow(x1, y1, x2, y2):
    canvas.create_line(
        x1, y1, x2, y2,
        arrow=tk.LAST,
        width=3
    )


def draw_question():
    canvas.delete("all")

    cy = 300
    missing = question["missing"]

    texts = [
        str(question["variable"]),
        "{} {}".format(*question["operations"][0]),
        "{} {}".format(*question["operations"][1]),
        format_expr(question["result"]),
    ]

    for i in range(4):
        draw_box(i, None if i == missing else texts[i])

    # Put the entry field inside the missing box.
    answer_entry.config(width=4 if missing == 0 else 6 if missing in (1, 2) else 11)
    canvas.create_window(POSITIONS[missing], cy, window=answer_entry)

    for i in range(3):
        draw_arrow(
            POSITIONS[i] + box_width(i) / 2,
            cy,
            POSITIONS[i + 1] - box_width(i + 1) / 2,
            cy
        )

    canvas.create_text(
        WIDTH / 2,
        100,
        text="NUMBER MACHINE",
        font=("Arial", 28, "bold")
    )


def set_state(state):
    bg, border = COLOURS[state]
    answer_entry.config(
        bg=bg,
        highlightbackground=border,
        highlightcolor=border
    )


# --------------------------------------------------
# EVALUATING ANSWERS
# --------------------------------------------------

def evaluate(entered):
    """
    Returns one of:
      "empty"       nothing typed
      "incomplete"  could still become correct (or can't be read yet)
      "correct"
      "wrong"       obviously wrong, whatever is typed next
      "maybe_wrong" a complete expression that doesn't match (yet)
    """
    entered = entered.strip()

    if not entered:
        return "empty"

    missing = question["missing"]
    var = question["variable"]

    # Missing input: just the variable letter.
    if missing == 0:
        return "correct" if entered.lower() == str(var) else "wrong"

    # Missing operation, e.g. "x 5" or "/ 3".
    if missing in (1, 2):
        cleaned = re.sub(r"\s+", "", entered.lower())
        cleaned = cleaned.replace("×", "x").replace("*", "x").replace("÷", "/")

        match = re.fullmatch(r"([x+\-/])(\d*)", cleaned)

        if not match:
            return "wrong"

        symbol, digits = match.groups()
        correct_symbol, correct_number = question["operations"][missing - 1]

        if symbol != correct_symbol:
            return "wrong"

        if not digits:
            return "incomplete"

        target = str(correct_number)

        if digits == target:
            return "correct"
        if target.startswith(digits):
            return "incomplete"
        return "wrong"

    # Missing output: an algebraic expression.
    try:
        student = parse_expr(
            entered.lower().replace("^", "**").replace("×", "*").replace("÷", "/"),
            local_dict=SYMBOLS,
            transformations=TRANSFORMS
        )
    except Exception:
        return "incomplete"

    if not isinstance(student, sp.Basic):
        return "incomplete"

    # Wrong variable letter: obviously wrong straight away.
    if student.free_symbols - {var}:
        return "wrong"

    if sp.simplify(student - question["result"]) == 0:
        return "correct"

    return "maybe_wrong"


def cancel_pending():
    global pending_job

    if pending_job is not None:
        root.after_cancel(pending_job)
        pending_job = None


def show_wrong():
    global pending_job

    pending_job = None
    set_state("wrong")
    feedback.config(text="Not quite. Try again.", fg="red")


def on_change(*_):
    """Runs on every keystroke."""
    global pending_job

    cancel_pending()

    if question is None:
        return

    result = evaluate(answer_var.get())

    if result == "correct":
        set_state("correct")
        feedback.config(text="Correct!", fg="green")

    elif result == "wrong":
        show_wrong()

    else:
        set_state("neutral")
        feedback.config(text="")

        if result == "maybe_wrong":
            pending_job = root.after(WRONG_DELAY, show_wrong)


def check_answer():
    """Enter key: gives a final verdict straight away."""
    cancel_pending()

    result = evaluate(answer_var.get())

    if result == "correct":
        set_state("correct")
        feedback.config(text="Correct!", fg="green")

    elif result == "empty":
        set_state("neutral")
        feedback.config(text="Please enter an answer.", fg="red")

    elif result == "incomplete":
        set_state("wrong")
        if question["missing"] in (1, 2):
            feedback.config(
                text="Enter an operation and a number, e.g. x 5",
                fg="red"
            )
        else:
            feedback.config(text="I couldn't understand that answer.", fg="red")

    else:
        show_wrong()


# --------------------------------------------------
# NEXT QUESTION
# --------------------------------------------------

def new_question():
    global question

    cancel_pending()
    question = make_question()

    answer_var.set("")
    set_state("neutral")
    draw_question()

    question_label.config(text=question["instruction"])
    feedback.config(text="")

    answer_entry.focus_set()


def background_click(event):
    """Any click on white space (not on a box, arrow or the answer field)."""
    widget = event.widget

    if widget is canvas:
        items = canvas.find_overlapping(
            event.x - 2,
            event.y - 2,
            event.x + 2,
            event.y + 2
        )
        if not items:
            new_question()

    elif widget in (root, question_label, feedback):
        new_question()


# --------------------------------------------------
# KEYBOARD AND MOUSE
# --------------------------------------------------

answer_var.trace_add("write", on_change)
answer_entry.bind("<Return>", lambda event: check_answer())
root.bind("<Button-1>", background_click)
root.bind_all("<Escape>", lambda event: root.destroy())

new_question()
root.mainloop()