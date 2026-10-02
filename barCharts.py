import matplotlib.pyplot as plt
import numpy as np

categ = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 3, 1, 5, 3, 6])

plt.bar(categ, values, color="crimson")

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")




plt.show()