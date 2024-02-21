import numpy as np
import matplotlib.pyplot as plt

# function
def f(x):
    return x**10 - 1

# bisection method
def bisection(f, a, b, tol=1e-3):
    if f(a) * f(b) > 0:
        raise ValueError("Function has same signs at the ends of the interval")

    while abs(a - b) >= tol:
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol:
            return c
        if f(a) * fc < 0:
            b = c
        elif f(b) * fc < 0:
            a = c
    return c

# false position method
def false_position(f, x0, x1, tol=1e-3, max_iter=1000):
    for i in range(max_iter):
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


root_bisection = bisection(f, 0, 1.3)
root_false_position = false_position(f, 0, 1.3)

# Print the results
print(f"Bisection method root: {root_bisection}")
print(f"False position method root: {root_false_position}")

# Plotting the function and roots
x_values = np.linspace(0, 1.3, 400)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$f(x) = x^{10} - 1$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(root_bisection, color='r', linestyle='--', label=f'Bisection Root: {root_bisection:.3f}')
plt.axvline(root_false_position, color='g', linestyle=':', label=f'False Position Root: {root_false_position:.3f}')
plt.title('Root Finding with Bisection and False Position Methods')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
