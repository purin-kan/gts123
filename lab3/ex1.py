import matplotlib.pyplot as plt
import numpy as np
import math as m

# Create an array of x values using an equation (e.g., x = sin(t))
x = np.arange(-m.pi*3, m.pi*3, 0.1)

# Calculate corresponding y values using another equation (e.g., y = cos(t))
y1 = np.sin(x)
y2 = np.sin(x + 0.5)
y3 = np.sin(x + 1)
y4 = np.sin(x + 1.5)

# Create a plot
plt.plot(x, y1 , color ="blue", linestyle="dotted")
plt.plot(x, y2 , color ="green", linestyle="dashdot")
plt.plot(x, y3 , color ="orange", linestyle="dashed")
plt.plot(x, y4 , color ="gray", linestyle="solid")

# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# Display the plot
plt.show()