
import tkinter as tk
import random

# ---------------- SETTINGS ----------------

MIN_ROWS = 7
MAX_ROWS = 7
MAX_FREQUENCY = 5

numbers = []
frequencies = []
product_entries = []


# ---------------- CALCULATIONS ----------------

def calculate_answers():
    global correct_mode
    global correct_mean, correct_total, correct_total_frequency

    # Mode
    max_freq = max(frequencies)
    correct_mode = numbers[frequencies.index(max_freq)]

    # Totals
    correct_total_frequency = sum(frequencies)

    correct_total = sum(
        n * f for n, f in zip(numbers, frequencies)
    )

    # Mean
    correct_mean = correct_total / correct_total_frequency


# ---------------- NEW QUESTION ----------------

def new_question():

    global numbers, frequencies
    global frequency_total_entry, product_total_entry

    # Destroy changing table contents
    for item in data_frame.winfo_children():
        item.destroy()

    rows = random.randint(MIN_ROWS, MAX_ROWS)

    numbers = sorted(random.sample(range(101), rows))

    frequencies = [
        random.randint(1, MAX_FREQUENCY)
        for _ in range(rows)
    ]

    # Ensure a unique mode
    mode_index = random.randrange(rows)
    frequencies[mode_index] = MAX_FREQUENCY + 1

    calculate_answers()

    headings = [
        "Price",
        "Quantity",
        "Cost"
    ]

    for col, heading in enumerate(headings):
        tk.Label(
            data_frame,
            text=heading,
            font=("Arial", 13, "bold"),
            width=19
        ).grid(row=0, column=col, padx=5, pady=6)

    product_entries.clear()

    # Display table
    for row in range(rows):

        tk.Label(
            data_frame,
            text=str(numbers[row]),
            font=("Arial", 14),
            width=12
        ).grid(row=row + 1, column=0, pady=3)

        tk.Label(
            data_frame,
            text=str(frequencies[row]),
            font=("Arial", 14),
            width=12
        ).grid(row=row + 1, column=1, pady=3)

        # Product entry
        entry = tk.Entry(
            data_frame,
            font=("Arial", 14),
            width=12,
            justify="center"
        )

        entry.grid(row=row + 1, column=2, pady=3)

        product_entries.append(entry)

    # Total row
    total_row = rows + 1

    tk.Label(
        data_frame,
        text="TOTAL",
        font=("Arial", 14, "bold"),
        width=12
    ).grid(row=total_row, column=0, pady=(10, 3))

    frequency_total_entry = tk.Entry(
        data_frame,
        font=("Arial", 14),
        width=12,
        justify="center"
    )
    frequency_total_entry.grid(row=total_row, column=1, pady=(10, 3))

    product_total_entry = tk.Entry(
        data_frame,
        font=("Arial", 14),
        width=12,
        justify="center"
    )
    product_total_entry.grid(row=total_row, column=2, pady=(10, 3))

    # Clear feedback
    product_feedback.config(text="")
    frequency_total_feedback.config(text="")
    product_total_feedback.config(text="")

    # Clear statistical answers
    for entry in answer_entries.values():
        entry.delete(0, tk.END)

    for label in feedback_labels.values():
        label.config(text="")


# ---------------- CHECK PRODUCTS ----------------

def check_products():

    all_correct = True
    errors = []

    for i in range(len(numbers)):

        correct = numbers[i] * frequencies[i]

        try:
            answer = int(product_entries[i].get())

            if answer == correct:
                product_entries[i].config(bg="light green")
            else:
                product_entries[i].config(bg="misty rose")
                errors.append(
                    f"{numbers[i]}: correct answer = {correct}"
                )
                all_correct = False

        except ValueError:
            product_entries[i].config(bg="misty rose")
            errors.append(
                f"{numbers[i]}: correct answer = {correct}"
            )
            all_correct = False

    if all_correct:
        product_feedback.config(
            text="All products correct!",
            fg="green"
        )
    else:
        product_feedback.config(
            text="Wrong: " + " | ".join(errors),
            fg="red"
        )


# ---------------- CHECK FREQUENCY TOTAL ----------------

def check_frequency_total():

    try:
        answer = int(frequency_total_entry.get())

        if answer == correct_total_frequency:
            frequency_total_entry.config(bg="light green")
            frequency_total_feedback.config(
                text="Correct!",
                fg="green"
            )
        else:
            frequency_total_entry.config(bg="misty rose")
            frequency_total_feedback.config(
                text=f"Wrong – correct answer: {correct_total_frequency}",
                fg="red"
            )

    except ValueError:
        frequency_total_entry.config(bg="misty rose")
        frequency_total_feedback.config(
            text="Enter a whole number",
            fg="red"
        )


# ---------------- CHECK PRODUCT TOTAL ----------------

def check_product_total():

    try:
        answer = int(product_total_entry.get())

        if answer == correct_total:
            product_total_entry.config(bg="light green")
            product_total_feedback.config(
                text="Correct!",
                fg="green"
            )
        else:
            product_total_entry.config(bg="misty rose")
            product_total_feedback.config(
                text=f"Wrong – correct answer: {correct_total}",
                fg="red"
            )

    except ValueError:
        product_total_entry.config(bg="misty rose")
        product_total_feedback.config(
            text="Enter a whole number",
            fg="red"
        )


# ---------------- CHECK STATISTICAL ANSWERS ----------------

def check_answer(name):

    try:
        answer = float(answer_entries[name].get())

        correct = {
            "Mode": correct_mode,
            "Mean": correct_mean
        }[name]

        if abs(answer - correct) < 0.005:
            feedback_labels[name].config(
                text="Correct!",
                fg="green"
            )

        else:
            correct_text = (
                f"{correct:.2f}" if name == "Mean"
                else str(correct)
            )

            feedback_labels[name].config(
                text=f"Wrong – correct answer: {correct_text}",
                fg="red"
            )

    except ValueError:
        feedback_labels[name].config(
            text="Enter a valid number",
            fg="red"
        )


# ---------------- SHOW ALL ANSWERS ----------------

def show_answers():

    # Fill products
    for i in range(len(numbers)):

        correct = numbers[i] * frequencies[i]

        product_entries[i].delete(0, tk.END)
        product_entries[i].insert(0, str(correct))
        product_entries[i].config(bg="light green")

    # Fill frequency total
    frequency_total_entry.delete(0, tk.END)
    frequency_total_entry.insert(
        0, str(correct_total_frequency)
    )
    frequency_total_entry.config(bg="light green")

    # Fill product total
    product_total_entry.delete(0, tk.END)
    product_total_entry.insert(0, str(correct_total))
    product_total_entry.config(bg="light green")

    # Fill mode and mean
    answers = {
        "Mode": str(correct_mode),
        "Mean": f"{correct_mean:.2f}"
    }

    for name, answer in answers.items():

        answer_entries[name].delete(0, tk.END)
        answer_entries[name].insert(0, answer)

        feedback_labels[name].config(
            text="Answer shown",
            fg="green"
        )

    product_feedback.config(
        text="All answers shown",
        fg="green"
    )

    frequency_total_feedback.config(text="")
    product_total_feedback.config(text="")


# ---------------- WINDOW ----------------

root = tk.Tk()
root.title("Frequency Tables")
root.geometry("1350x1050")

tk.Label(
    root,
    text="Frequency Tables",
    font=("Arial", 24, "bold")
).pack(pady=15)


# ---------------- TABLE FRAMES ----------------

table_frame = tk.Frame(root)
table_frame.pack(pady=10)

data_frame = tk.Frame(table_frame)
data_frame.pack()


# ---------------- PRODUCT CHECKING ----------------

product_feedback = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    wraplength=1300
)
product_feedback.pack(pady=5)

tk.Button(
    root,
    text="Check Costs",
    font=("Arial", 14),
    command=check_products
).pack(pady=8)


# ---------------- TOTAL CHECKING ----------------

total_frame = tk.Frame(root)
total_frame.pack(pady=8)

tk.Button(
    total_frame,
    text="Check Total Quantity",
    font=("Arial", 13),
    command=check_frequency_total
).pack(side="left", padx=8)

frequency_total_feedback = tk.Label(
    total_frame,
    text="",
    font=("Arial", 13, "bold")
)
frequency_total_feedback.pack(side="left", padx=8)

tk.Button(
    total_frame,
    text="Check Total Cost",
    font=("Arial", 13),
    command=check_product_total
).pack(side="left", padx=8)

product_total_feedback = tk.Label(
    total_frame,
    text="",
    font=("Arial", 13, "bold")
)
product_total_feedback.pack(side="left", padx=8)


# ---------------- STATISTICAL ANSWERS ----------------

answer_entries = {}
feedback_labels = {}

for name in ["Mode", "Mean"]:

    frame = tk.Frame(root)
    frame.pack(pady=8)

    tk.Label(
        frame,
        text=name + ":",
        font=("Arial", 16),
        width=10,
        anchor="w"
    ).pack(side="left")

    entry = tk.Entry(
        frame,
        font=("Arial", 16),
        width=12,
        justify="center"
    )
    entry.pack(side="left", padx=8)

    answer_entries[name] = entry

    tk.Button(
        frame,
        text="Check",
        font=("Arial", 12),
        command=lambda n=name: check_answer(n)
    ).pack(side="left", padx=5)

    feedback = tk.Label(
        frame,
        text="",
        font=("Arial", 13, "bold"),
        width=35,
        anchor="w"
    )
    feedback.pack(side="left", padx=5)

    feedback_labels[name] = feedback


# ---------------- MAIN BUTTONS ----------------

tk.Button(
    root,
    text="Show Answers",
    font=("Arial", 15, "bold"),
    command=show_answers
).pack(pady=12)

tk.Button(
    root,
    text="New Question",
    font=("Arial", 16, "bold"),
    command=new_question
).pack(pady=15)


# ---------------- START ----------------

new_question()

root.mainloop()
