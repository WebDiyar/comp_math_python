import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# Define the functions and their corresponding phi(x) functions
def f1(x):
    return x**3 - 9*x + 1

def phi1(x):
    return (9*x - 1)**(1/3)

def f2(x):
    return x - 0.3 - np.sin(x)

def phi2(x):
    return 0.3 + np.sin(x)

def f3(x):
    return np.exp(x) - 5*x

def phi3(x):
    return np.exp(x)/5

# Iteration method
def iteration_method(f, phi, a, b, tol=1e-3, max_iter=100):
    x0 = (a + b) / 2
    for _ in range(max_iter):
        x1 = phi(x0)
        if abs(f(x1) - f(x0)) < tol:
            return x1
        x0 = x1
    return x0  # Return the last approximation if tolerance is not met

# Find intervals
a1, b1 = 0, 1
a2, b2 = 0, 2
a3, b3 = 1, 2

# Apply the iteration method
root1 = iteration_method(f1, phi1, a1, b1)
root2 = iteration_method(f2, phi2, a2, b2)
root3 = iteration_method(f3, phi3, a3, b3)

print(root1);
print(root2);
print(root3);

# Setting up the plot range
x_range = np.linspace(-2, 4, 400)

# Plotting the functions and the roots
plt.figure(figsize=(12, 8))

# Plot for x^3 - 9x + 1 = 0
plt.plot(x_range, f1(x_range), label=r'$x^3 - 9x + 1 = 0$', color='blue')
plt.scatter([root1], [f1(root1)], color='blue', marker='o')

# Plot for x = 0.3 + sin(x)
plt.plot(x_range, f2(x_range), label=r'$x = 0.3 + \sin(x)$', color='green')
plt.scatter([root2], [f2(root2)], color='green', marker='o')

# Plot for e^x = 5x
plt.plot(x_range, f3(x_range), label=r'$e^x = 5x$', color='red')
plt.scatter([root3], [f3(root3)], color='red', marker='o')

# Adding labels and legend
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.title('Graphs of the Functions with Identified Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# Show plot
plt.show()
