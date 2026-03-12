# Import libraries
from matplotlib import pyplot as plt
import numpy as np

N = 17
D = 12
M = N - D
fraction = f"{N}/{D}"
labels1 = [f"{n}" for n in range(1, D+1)]
labels2 = [f"{n}" for n in range(D+1, D+M+1)]
labels2.append("")

# Creating plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), num=f"{fraction}")
ax1.pie([1]*D, labels=labels1)
x = [1]*M
x.append(9)
ax2.pie(x, labels=labels2)
plt.show()