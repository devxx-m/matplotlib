import matplotlib.pyplot as plt
import numpy as np


x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([0, 43, 10, 100])
y3 = np.array([40, 5, 18, 50])

line_style = dict(marker = ".", 
                markersize = 15, 
                markerfacecolor="#1cd3fc",
                markeredgecolor = "black",
                linestyle = "solid",
            )


plt.plot(x, y1,color="red", **line_style)
plt.plot(x, y2,color="purple", **line_style)
plt.plot(x, y3,color="blue", **line_style)

plt.show()