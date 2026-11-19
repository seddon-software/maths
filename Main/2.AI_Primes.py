
import tkinter as tk
import random
import math

# Settings
NUMBER_COUNT = 25
TARGET_COUNT = 5
MIN_NUMBER = 2
MAX_NUMBER = 99

WIDTH = 1200
HEIGHT = 750

FONT = ("Arial", 26, "bold")
NEW_GAME_DISTANCE = 60

# Random challenge selection
SEARCH_OPTIONS = [
    ("prime", 3),
    ("odd", 1),
    ("even", 1),
    ("multiple of 7", 1),
    ("divisible by 8", 1)
]


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False

    return True


def is_target(n):
    if SEARCH_FOR == "prime":
        return is_prime(n)

    elif SEARCH_FOR == "odd":
        return n % 2 != 0

    elif SEARCH_FOR == "even":
        return n % 2 == 0

    elif SEARCH_FOR == "multiple of 7":
        return n % 7 == 0

    elif SEARCH_FOR == "divisible by 8":
        return n % 8 == 0

    return False


def new_game(event=None):
    global found, game_over, positions, SEARCH_FOR

    canvas.delete("all")

    found = 0
    game_over = False

    # Randomly select challenge (prime is 3 times more likely)
    options = [item[0] for item in SEARCH_OPTIONS]
    weights = [item[1] for item in SEARCH_OPTIONS]

    SEARCH_FOR = random.choices(
        options, weights=weights, k=1
    )[0]

    # Separate target and non-target numbers
    targets = [
        n for n in range(MIN_NUMBER, MAX_NUMBER + 1)
        if is_target(n)
    ]

    others = [
        n for n in range(MIN_NUMBER, MAX_NUMBER + 1)
        if not is_target(n)
    ]

    selected_targets = random.sample(targets, TARGET_COUNT)

    selected_others = random.sample(
        others, NUMBER_COUNT - TARGET_COUNT
    )

    numbers = selected_targets + selected_others
    random.shuffle(numbers)

    # Distribute numbers across canvas
    positions = []

    for _ in numbers:
        while True:
            x = random.randint(60, WIDTH - 60)
            y = random.randint(60, HEIGHT - 60)

            if all(
                math.hypot(x - px, y - py) > 85
                for px, py in positions
            ):
                positions.append((x, y))
                break

    # Draw numbers
    for number, (x, y) in zip(numbers, positions):

        tag = f"number_{number}_{x}_{y}"

        canvas.create_text(
            x, y,
            text=str(number),
            fill="black",
            font=FONT,
            tags=(tag, "number")
        )

        canvas.tag_bind(
            tag,
            "<Button-1>",
            lambda event, n=number, t=tag: click_number(n, t)
        )

    status.config(
        text=f"Find the {TARGET_COUNT} {SEARCH_FOR} numbers!"
    )


def click_number(number, tag):
    global found, game_over

    if game_over:
        return

    if is_target(number):

        canvas.itemconfig(tag, fill="red")
        canvas.tag_unbind(tag, "<Button-1>")

        found += 1

        status.config(
            text=f"Found: {found} / {TARGET_COUNT}"
        )

        if found == TARGET_COUNT:
            game_over = True
            status.config(text="Well done! You found them all!")

    else:
        game_over = True

        canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            text="💣",
            font=("Arial", 110),
            fill="red",
            tags="bomb"
        )

        status.config(
            text=f"BOOM! {number} is not a {SEARCH_FOR} number!"
        )


def background_click(event):
    # New game only when clicking sufficiently far from numbers
    for x, y in positions:
        distance = math.hypot(event.x - x, event.y - y)

        if distance < NEW_GAME_DISTANCE:
            return

    new_game()


# Main window
root = tk.Tk()
root.title("Number Challenge")
root.geometry(f"{WIDTH}x{HEIGHT + 80}")

# Escape quits
root.bind("<Escape>", lambda event: root.destroy())

# Status display
status = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold")
)
status.pack(pady=10)

# Canvas
canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="white",
    highlightthickness=0
)
canvas.pack()

# Clicking distant white space starts another game
canvas.bind("<Button-1>", background_click)

# Start first game
new_game()

root.mainloop()
