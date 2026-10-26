"""
Open AQA GCSE Maths Foundation Tier Papers in Browser (June 2023 - Nov 2022)
------------------------------------------------------------------------------
Opens each Foundation tier question paper in your default browser, one at a
time, so you can view/save them yourself.

Usage:
    python open_foundation_papers_2022_2023.py
"""

import webbrowser
import time

PAPERS = {
    "June 2023 Paper 1 (Non-Calc)": "https://cdn.sanity.io/files/p28bar15/green/fcdbf36e862a5bace99010065418381a4c2955d0.pdf",
    "June 2023 Paper 2 (Calc)": "https://cdn.sanity.io/files/p28bar15/green/1170ee44760aa53249c184343b19e67944c49a52.pdf",
    "June 2023 Paper 3 (Calc)": "https://cdn.sanity.io/files/p28bar15/green/ecd22bc86812e1d31d182d51aabd7c22f292f2e5.pdf",
    "Nov 2022 Paper 1 (Non-Calc)": "https://cdn.sanity.io/files/p28bar15/green/cbcd375a0a3162872a541455d298ecce4e738606.pdf",
    "Nov 2022 Paper 2 (Calc)": "https://cdn.sanity.io/files/p28bar15/green/ccb1fee34025f26bcae54f8d48d48d765c3cc6b3.pdf",
    "Nov 2022 Paper 3 (Calc)": "https://cdn.sanity.io/files/p28bar15/green/689b0eab8f821f31a805c0f46b31da9b467458f4.pdf",
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

