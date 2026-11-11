import tkinter as tk

ROWS, COLS = 2, 4
SEPARATORS = [":", ":", "="]
MULTIPLIER = 15   # row 2 = row 1 x MULTIPLIER (must be a whole number)
ROW_COLORS = ["#90ee90", "#00ffff"]   # row 1 light green, row 2 cyan
STAR_COLOR = "red"
TEXT_COLOR = "black"

# Use whole numbers or '*' (unknown), with at most one '*' per column.
values = [
#   [1,   4,   3,    8],
#   [15,  60,  45,   120],
    [1,   "*", 3,    "*"],   # row 1
    ["*", 60,   "*", 120],   # row 2 (multiple of row 1)
]

def validate():
    if not isinstance(MULTIPLIER, int) or MULTIPLIER == 0:
        raise ValueError("MULTIPLIER must be a non-zero integer")

    for r in range(ROWS):
        for c in range(COLS):
            v = values[r][c]
            if v != "*" and not isinstance(v, int):
                raise ValueError(f"Row {r+1}, column {c+1} must be an integer or '*'")

    for c in range(COLS):
        if sum(1 for r in range(ROWS) if values[r][c] == "*") > 1:
            raise ValueError(f"Column {c+1} has more than one '*'")

        # A '*' in row 1 is row 2 / MULTIPLIER, so row 2 must divide evenly
        if values[0][c] == "*" and values[1][c] % MULTIPLIER != 0:
            raise ValueError(
                f"Row 1, column {c+1} would not be an integer: "
                f"{values[1][c]} is not divisible by {MULTIPLIER}"
            )

validate()

def text_color(v):
    return STAR_COLOR if v == "*" else TEXT_COLOR

def calculate(r, c):
    """Integer value for cell (r, c), taken from the other row in the same column."""
    other = values[1 - r][c]
    if r == 1:
        return other * MULTIPLIER    # row 2 = row 1 x MULTIPLIER
    return other // MULTIPLIER       # row 1 = row 2 / MULTIPLIER (exact, checked above)

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

root = tk.Tk()
root.title("Ratios")

buttons = [[None] * COLS for _ in range(ROWS)]

for r in range(ROWS):
    root.rowconfigure(r, weight=1)
    for c in range(COLS):
        col = c * 2
        root.columnconfigure(col, weight=1)

        btn = tk.Button(
            root,
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
        btn.grid(row=r, column=col, padx=5, pady=5, sticky="nsew")
        buttons[r][c] = btn

        if c < COLS - 1:
            tk.Label(root, text=SEPARATORS[c], font=("Arial", 30, "bold")).grid(
                row=r, column=col + 1
            )

root.mainloop()