import numpy as np
import matplotlib.pyplot as plt

# Define the interval
x = np.linspace(-np.pi/2, np.pi/2, 400)
y = np.tan(x)

# Handle asymptotes by setting large values to NaN
y[np.abs(y) > 10] = np.nan

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = tan(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(-10, 10)
plt.xlim(-np.pi/2, np.pi/2)
plt.title('Graph of y = tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
