import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)  # Color for each point
sizes = 1000 * np.random.rand(50)  # Size of each point

# Create the scatter plot
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot')
plt.savefig('scatter_plot.png')

# Show the plot
plt.show()