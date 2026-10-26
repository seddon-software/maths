"""
Open AQA GCSE Maths Foundation Tier Papers in Browser
-------------------------------------------------------
Opens each Foundation tier question paper (Nov 2024 - June 2025) in your
default browser, one at a time, so you can view/save them yourself.

Usage:
    python open_foundation_papers.py
"""

import webbrowser
import time

PAPERS = {
    "June 2025 Paper 1 (Non-Calc)": "https://cdn.sanity.io/files/p28bar15/green/e1b7736f029e91ae154d9a08fd85dfeed7d83e84.pdf",
    "June 2025 Paper 2 (Calc)": "https://cdn.sanity.io/files/p28bar15/green/98aa5c29eb33cb6f531f21d21cb1c5d3e22e53e2.pdf",
    "June 2025 Paper 3 (Calc)": "https://cdn.sanity.io/files/p28bar15/green/7636c65f12cb16a821c69d974095a33258f18749.pdf",
    "Nov 2024 Paper 1 (Non-Calc)": "https://cdn.sanity.io/files/p28bar15/green/d7131939f5fcfc425c7068d43b28b6ddde2791f4.pdf",
    "Nov 2024 Paper 2 (Calc)": "https://cdn.sanity.io/files/p28bar15/green/b15ebd2dd1a3cf6c788ae4b05733a21efdb1df5d.pdf",
    "Nov 2024 Paper 3 (Calc)": "https://cdn.sanity.io/files/p28bar15/green/4b1c711fb616368047bf91f212f207541bdaff76.pdf",
}

DELAY_SECONDS = 2.0  # gap between opening each tab, so the browser doesn't choke


def open_papers():
    for name, url in PAPERS.items():
        print(f"Opening: {name}")
        webbrowser.open(url)
        time.sleep(DELAY_SECONDS)

    print("\nDone - all papers opened in your browser.")


if __name__ == "__main__":
    open_papers()

