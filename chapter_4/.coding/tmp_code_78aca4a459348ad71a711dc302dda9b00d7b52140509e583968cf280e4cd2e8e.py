import matplotlib.pyplot as plt
import numpy as np

# Create data
y = np.random.rand(100)
x = np.arange(100)

# Create a simple plot
plt.plot(x, y)
plt.title('Simple Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()