"""
AQA GCSE Maths Past Paper Opener
---------------------------------
Opens AQA's past-papers pages in your default browser, one at a time,
so you can click "Download" yourself. Nothing here scrapes or automates
clicks on AQA's site - it just saves you typing/searching.

AQA GCSE Maths (8300) has 3 papers per series:
  Paper 1 - Non-Calculator
  Paper 2 - Calculator
  Paper 3 - Calculator
Each at Foundation (F) or Higher (H) tier.

Usage:
    python aqa_maths_paper_opener.py

It will open the official "Find past papers" tool pre-filtered to
GCSE Maths, plus (optionally) direct filestore links for specific
series if you already know which ones you want.
"""

import webbrowser
import time

# The official AQA tool - this is the safe, sanctioned starting point.
FINDER_URL = "https://www.aqa.org.uk/find-past-papers-and-mark-schemes"

# Direct assessment-resources page for GCSE Maths, filtered to question papers.
ASSESSMENT_RESOURCES_URL = (
    "https://www.aqa.org.uk/subjects/mathematics/gcse/mathematics-8300/"
    "assessment-resources?f.Resource+type%7C6=Question+papers&sort=title"
)

# Known direct filestore PDF pattern (confirm each link still resolves -
# AQA only keeps papers live for ~3 years, so older links may 404).
FILESTORE_TEMPLATE = (
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/"
    "{year}/{month}/AQA-8300{paper}{tier}-QP-{mon}{yy}.PDF"
)


def open_finder():
    """Open AQA's official past-papers search tool."""
    print(f"Opening: {FINDER_URL}")
    webbrowser.open(FINDER_URL)


def open_assessment_resources():
    """Open the GCSE Maths assessment resources page, filtered to question papers."""
    print(f"Opening: {ASSESSMENT_RESOURCES_URL}")
    webbrowser.open(ASSESSMENT_RESOURCES_URL)


def open_specific_papers(series_list, delay=2.0):
    """
    Open a set of specific paper pages one by one.

    series_list: list of dicts like
        {"year": "2023", "month": "june", "mon": "JUN", "yy": "23", "paper": "1", "tier": "H"}

    Each tab opens `delay` seconds apart so your browser doesn't choke on
    opening 20 tabs at once. Check the URL actually resolves before relying
    on it - older series get taken down after ~3 years.
    """
    for s in series_list:
        url = FILESTORE_TEMPLATE.format(**s)
        print(f"Opening: {url}")
        webbrowser.open(url)
        time.sleep(delay)


if __name__ == "__main__":
    print("AQA GCSE Maths (8300) Past Paper Opener\n")
    print("1) Open official past-papers finder (recommended starting point)")
    print("2) Open GCSE Maths assessment resources page directly")
    print("3) Open a specific list of papers (edit the script to set them)")
    choice = input("Choose 1, 2, or 3: ").strip()

    if choice == "1":
        open_finder()
    elif choice == "2":
        open_assessment_resources()
    elif choice == "3":
        # Example - edit this list with the series you actually want.
        papers = [
            {"year": "2023", "month": "june", "mon": "JUN", "yy": "23", "paper": "1", "tier": "H"},
            {"year": "2023", "month": "june", "mon": "JUN", "yy": "23", "paper": "2", "tier": "H"},
            {"year": "2023", "month": "june", "mon": "JUN", "yy": "23", "paper": "3", "tier": "H"},
        ]
        open_specific_papers(papers)
    else:
        print("No valid option chosen.")

