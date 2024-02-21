import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
import math

# Functions
def f1(x):
    return x**3 - x - 1

def f2(x):
    return x * np.exp(x) - 2

def f3(x):
    return np.cos(x) - 3*x + 1

def f4(x):
    if x <= 0:
        return float('inf')
    return 2*x - np.log10(x) - 7

# Define the method of false position (regula falsi)
def false_position(f, x0, x1, tol=1e-3, max_iter=100):
    for _ in range(max_iter):
        y0, y1 = f(x0), f(x1)
        x2 = x0 - y0 * (x1 - x0) / (y1 - y0)
        y2 = f(x2)

        if abs(y2) < tol:
            return x2

        if y0 * y2 < 0:
            x1 = x2
        else:
            x0 = x2
    return x2

# Find roots using false position
root1 = false_position(f1, 1, 2)
root2 = false_position(f2, 0, 1)
root3 = false_position(f3, 0, 1)
root4 = false_position(f4, 1, 3)

# Create a range of x values for plotting
x_values = np.linspace(-2, 2, 400)

# Plot all the functions and their roots
plt.figure(figsize=(12, 8))
plt.plot(x_values, f1(x_values), label='x^3 - 5x + 1 = 0')
plt.plot(root1, f1(root1), 'ro')  # Root of f1
plt.plot(x_values, f2(x_values), label='x*e^(x) - 2 = 0')
plt.plot(root2, f2(root2), 'ro')  # Root of f2
plt.plot(x_values, f3(x_values), label='cos(x) - 3x + 1 = 0')
plt.plot(root3, f3(root3), 'ro')  # Root of f3
plt.plot(x_values, [f4(x) for x in x_values], label='2x - log(x) - 7 = 0')
plt.plot(root4, f4(root4), 'ro')  # Root of f4

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.title('Graphs of Functions and Their Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# Print the roots

print('Root of (i): ', root1);
print('Root of (ii): ',  root2);
print('Root of (iii): ', root3);
print('Root of (iv): ', root4);
