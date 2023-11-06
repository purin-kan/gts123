import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 10.1, 0.1)

y = (1 + x)/np.sqrt(x)

plt.plot(x, y , color ="blue", linestyle="solid")

plt.show()