percent = 101

# Import libraries
from matplotlib import pyplot as plt
import numpy as np

D = 100
M = percent - D
fraction = f"{percent}/{D}"

# Creating plot
fig, ax = plt.subplots(1, 1, figsize=(12, 6), num=f"{fraction}")
ax.pie([percent, D - percent], labels=[f"{percent:.1f}%", f"{D - percent:.1f}%"])
plt.show()
