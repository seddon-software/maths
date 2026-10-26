import webbrowser as wb

paper=input("Which paper? (1/2/3): ")
url = f"https://www.savemyexams.com/gcse/maths/aqa/past-papers/paper-{paper}/"
wb.open(url)

