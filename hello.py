print("hello world")

import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.2, 2.8, 3.6, 3.0, 4.8])

# Perform cubic fitting
coefficients = np.polyfit(x, y, 3)

# Extract the coefficients
a, b, c, d = coefficients

# Print the coefficients
print(f"Cubic fit coefficients: a={a}, b={b}, c={c}, d={d}")

# Generate points for plotting the fitted curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a*x_fit**3 + b*x_fit**2 + c*x_fit + d

# Plot the original data and the fitted curve
plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, label='Cubic Fit', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
