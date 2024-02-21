import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
import math

def secant_method(func, x0, x1, epsilon, max_iterations=1000):
    for _ in range(max_iterations):
        f_x0 = func(x0)
        f_x1 = func(x1)
        if f_x1 - f_x0 == 0:
            return None

        x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))

        if np.abs(x2 - x1) / np.abs(x2) < epsilon:
            return x2

        x0, x1 = x1, x2

    return x2


# Defining the functions
def f1(x):
    return x - np.exp(-x)

def f2(x):
    return x**3 + x**2 + x + 7

# Applying the Secant method
root_f1 = secant_method(f1, 0, 1, 1e-3)
root_f2 = secant_method(f2, -2, -1, 1e-3)

print(root_f1);
print(root_f2);
# Plotting
x_range = np.linspace(-3, 3, 400)
plt.figure(figsize=(12, 8))

# Plotting f1 and its root
plt.plot(x_range, f1(x_range), label='f(x) = x - e^(-x)')
plt.plot(root_f1, f1(root_f1), 'ro', label=f'Root of f1: {root_f1:.3f}')

# Plotting f2 and its root
plt.plot(x_range, f2(x_range), label='f(x) = x^3 + x^2 + x + 7')
plt.plot(root_f2, f2(root_f2), 'go', label=f'Root of f2: {root_f2:.3f}')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Secant Method: Finding Roots of Functions')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
