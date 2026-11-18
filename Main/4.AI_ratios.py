import random
import tkinter as tk

ROWS, COLS = 2, 4
SEPARATORS = [":", ":", "="]
HEADINGS = ["Ava", "Bob", "Carly", "Total"]
HEADING_FONT = ("Arial", 28, "bold")
ROW_LABELS = ["Ratios", "Totals"]
ROW_LABEL_FONT = ("Arial", 28, "bold")
TITLE_TEXT = "Ratios"
TITLE_FONT = ("Arial", 40, "bold")
TITLE_COLOR = "red"
ROW_COLORS = ["#90ee90", "#00ffff"]
MIDDLE_COLOR = "#ffe680"
MIDDLE_FONT = ("Arial", 24, "bold")
MIDDLE_HIDDEN_TEXT = "?"
STAR_COLOR = "red"
TEXT_COLOR = "black"
SCREEN_PADDING = 0.10

TOGGLE_FONT = ("Arial", 18, "bold")
MODE_NAMES = {False: "Original", True: "Simple"}

RATIO_MIN, RATIO_MAX = 1, 10
MULTIPLIER_MIN, MULTIPLIER_MAX = 10, 50

DATA_GRID_ROWS = [1, 3]
MIDDLE_GRID_ROW = 2
COL_OFFSET = 1

# False = original mode, True = simple mode
simple_mode = False


def make_puzzle(simple):
    """Random multiplier and ratios; last column contains totals."""

    multiplier = random.randint(MULTIPLIER_MIN, MULTIPLIER_MAX)

    row1 = [
        random.randint(RATIO_MIN, RATIO_MAX)
        for _ in range(COLS - 1)
    ]
    row1.append(sum(row1))

    row2 = [v * multiplier for v in row1[:3]]
    row2.append(sum(row2))

    if simple:
        # Row 1 first three values shown, grand total in row 2 shown.
        # Everything else is hidden and can be deduced.
        vals = [
            row1[:3] + ["*"],
            ["*", "*", "*", row2[3]],
        ]
        return multiplier, vals

    vals = [row1, row2]

    # One column fully shown; hide one value in each other column
    full_col = random.randrange(COLS - 1)

    for c in range(COLS - 1):
        if c != full_col:
            vals[random.randrange(ROWS)][c] = "*"

    return multiplier, vals


MULTIPLIER, values = make_puzzle(simple_mode)


def validate(simple):

    if not isinstance(MULTIPLIER, int) or MULTIPLIER == 0:
        raise ValueError("MULTIPLIER must be a non-zero integer")

    if len(HEADINGS) != COLS:
        raise ValueError(f"HEADINGS needs exactly {COLS} entries")

    if len(ROW_LABELS) != ROWS:
        raise ValueError(f"ROW_LABELS needs exactly {ROWS} entries")

    if not 0 <= SCREEN_PADDING < 0.5:
        raise ValueError("SCREEN_PADDING must be between 0 and 0.5")

    for r in range(ROWS):
        for c in range(COLS):
            v = values[r][c]
            if v != "*" and not isinstance(v, int):
                raise ValueError(
                    f"Row {r+1}, column {c+1} must be an integer or '*'"
                )

    if simple:
        # Row 1: first three shown, total hidden
        if not all(isinstance(values[0][c], int) for c in range(3)):
            raise ValueError("Simple mode: row 1 values must all be shown")

        if values[0][3] != "*":
            raise ValueError("Simple mode: row 1 total must be hidden")

        # Row 2: first three hidden, total shown
        if not all(values[1][c] == "*" for c in range(3)):
            raise ValueError("Simple mode: row 2 values must be hidden")

        if not isinstance(values[1][3], int):
            raise ValueError("Simple mode: row 2 total must be shown")

        if values[1][3] % sum(values[0][:3]) != 0:
            raise ValueError("Simple mode: total does not divide evenly")

        return

    # Check totals when all three component values are visible
    for r in range(ROWS):
        if all(isinstance(v, int) for v in values[r][:3]):
            if values[r][3] != sum(values[r][:3]):
                raise ValueError(f"Row {r+1}: total is incorrect")

    # Check hidden values
    stars_per_column = [
        sum(1 for r in range(ROWS) if values[r][c] == "*")
        for c in range(COLS)
    ]

    if any(s > 1 for s in stars_per_column):
        raise ValueError("A column has more than one '*'")

    if stars_per_column[:3].count(0) != 1:
        raise ValueError(
            "Exactly one of the first three columns must be complete"
        )

    for c in range(COLS - 1):
        a, b = values[0][c], values[1][c]

        if "*" not in (a, b) and b != a * MULTIPLIER:
            raise ValueError(
                f"Column {c+1}: {b} != {a} x {MULTIPLIER}"
            )

        if a == "*" and b % MULTIPLIER != 0:
            raise ValueError(
                f"Row 1, column {c+1} would not be an integer"
            )

    # Check totals are consistent with multiplier
    if values[0][3] * MULTIPLIER != values[1][3]:
        raise ValueError("Totals do not match the multiplier")


def text_color(v):
    return STAR_COLOR if v == "*" else TEXT_COLOR


def calculate(r, c):
    """Calculate the missing value from the other row."""

    other = values[1 - r][c]

    if r == 1:
        return other * MULTIPLIER

    return other // MULTIPLIER


def on_click(r, c):

    if values[r][c] != "*":
        print(f"Clicked row {r+1}, column {c+1}: {values[r][c]}")
        return

    result = calculate(r, c)
    values[r][c] = result

    buttons[r][c].config(
        text=str(result),
        fg=text_color(result),
        activeforeground=text_color(result),
    )


def on_multiplier_click(c):

    # Reveal the multiplier in every column
    for btn in middle_buttons:
        btn.config(text=f"x{MULTIPLIER}")


def new_example():
    """Generate and display a new puzzle."""

    global MULTIPLIER, values

    MULTIPLIER, values = make_puzzle(simple_mode)
    validate(simple_mode)

    # Update data buttons
    for r in range(ROWS):
        for c in range(COLS):
            v = values[r][c]

            buttons[r][c].config(
                text=str(v),
                fg=text_color(v),
                activeforeground=text_color(v),
            )

    # Reset multiplier buttons
    for btn in middle_buttons:
        btn.config(text=MIDDLE_HIDDEN_TEXT)


def toggle_mode():
    """Switch between original and simple mode and start a new puzzle."""

    global simple_mode

    simple_mode = not simple_mode
    toggle_btn.config(text=f"Mode: {MODE_NAMES[simple_mode]}")
    new_example()


def on_background_click(event):
    """Generate a new puzzle only when clicking outside main."""

    widget = event.widget

    while widget is not None:
        if widget == main or widget == toggle_btn:
            return

        if widget == root:
            break

        widget = widget.master

    new_example()


# Validate initial puzzle
validate(simple_mode)


# --------------------------------------------------
# Tkinter window
# --------------------------------------------------

root = tk.Tk()
root.title(TITLE_TEXT)

# Start at the mouse pointer so fullscreen happens on that monitor
px, py = root.winfo_pointerxy()
root.geometry(f"800x600+{max(px - 400, 0)}+{max(py - 300, 0)}")
root.update()
root.attributes("-fullscreen", True)

# Esc closes the program completely, F11 toggles fullscreen
root.bind("<Escape>", lambda e: root.destroy())
root.bind("<F11>", lambda e: root.attributes(
    "-fullscreen", not root.attributes("-fullscreen")))

# Main container
main = tk.Frame(root)

main.place(
    relx=SCREEN_PADDING,
    rely=SCREEN_PADDING,
    relwidth=1 - 2 * SCREEN_PADDING,
    relheight=1 - 2 * SCREEN_PADDING,
)

# Title
title_label = tk.Label(
    root,
    text=TITLE_TEXT,
    font=TITLE_FONT,
    fg=TITLE_COLOR
)

title_label.place(
    relx=0.5,
    rely=SCREEN_PADDING / 2,
    anchor="center"
)

# Mode toggle button (top-right corner)
toggle_btn = tk.Button(
    root,
    text=f"Mode: {MODE_NAMES[simple_mode]}",
    font=TOGGLE_FONT,
    command=toggle_mode,
)

toggle_btn.place(relx=1.0, rely=0.0, x=-20, y=20, anchor="ne")

buttons = [[None] * COLS for _ in range(ROWS)]
middle_buttons = [None] * COLS

# Row label column
main.columnconfigure(0, weight=0)

# Heading row
for c in range(COLS):
    tk.Label(
        main,
        text=HEADINGS[c],
        font=HEADING_FONT
    ).grid(
        row=0,
        column=c * 2 + COL_OFFSET,
        pady=(10, 0)
    )

# Multiplier buttons
main.rowconfigure(MIDDLE_GRID_ROW, weight=0)

for c in range(COLS):

    mbtn = tk.Button(
        main,
        text=MIDDLE_HIDDEN_TEXT,
        font=MIDDLE_FONT,
        relief="flat",
        bg=MIDDLE_COLOR,
        activebackground=MIDDLE_COLOR,
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        command=lambda c=c: on_multiplier_click(c),
    )

    mbtn.grid(
        row=MIDDLE_GRID_ROW,
        column=c * 2 + COL_OFFSET,
        padx=5,
        pady=5,
        sticky="nsew"
    )

    middle_buttons[c] = mbtn

# Data rows
for r in range(ROWS):

    grid_row = DATA_GRID_ROWS[r]
    main.rowconfigure(grid_row, weight=1)

    # Row label
    tk.Label(
        main,
        text=ROW_LABELS[r],
        font=ROW_LABEL_FONT
    ).grid(
        row=grid_row,
        column=0,
        padx=(10, 5)
    )

    for c in range(COLS):

        col = c * 2 + COL_OFFSET

        main.columnconfigure(col, weight=1)

        btn = tk.Button(
            main,
            text=str(values[r][c]),
            width=10,
            height=3,
            font=("Arial", 40),
            relief="flat",
            bg=ROW_COLORS[r],
            activebackground=ROW_COLORS[r],
            fg=text_color(values[r][c]),
            activeforeground=text_color(values[r][c]),
            command=lambda r=r, c=c: on_click(r, c),
        )

        btn.grid(
            row=grid_row,
            column=col,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        buttons[r][c] = btn

        if c < COLS - 1:
            tk.Label(
                main,
                text=SEPARATORS[c],
                font=("Arial", 30, "bold")
            ).grid(
                row=grid_row,
                column=col + 1
            )


# Click outside the puzzle to generate a new example
root.bind("<Button-1>", on_background_click)

root.mainloop()