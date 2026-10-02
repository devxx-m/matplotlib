import matplotlib.pyplot as plt
import numpy as np


categ = np.array(["Freshmen", "Sophomores", "Juniors", "Seniors"])
values = np.array([300, 150, 275, 310])

colors = ["crimson", "cyan", "#8D8B55", "grey"]

plt.pie(values, labels=categ, autopct="%1.2f%%", colors=colors,
        explode=[0, 0, 0, 0.1],
        # shadow = True,
        startangle= 45
        )

plt.title("College")

plt.show()