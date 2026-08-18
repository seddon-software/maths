import matplotlib.pyplot as plt

from templates.straight_line import StraightLine


q = StraightLine()

q.generate()
q.solve()


fig, ax = plt.subplots(figsize=(7, 3))

q.draw(ax)

ax.set_aspect("equal")
ax.axis("off")

plt.title("Angles on a straight line")

print("----------------")
print("Question: Straight line")
print("Answer:", q.answer_text())

plt.show()
