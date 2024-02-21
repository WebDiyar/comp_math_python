import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
# Define the equation
def equation(x):
    return x^3 - 4x -9

# Define the derivative of the equation for Newton-Raphson method
def derivative_equation(x):
    return derivative(equation, x, dx=1e-6)
# Bisection method
def bisection_method(func, a, b, tolerance=1e-3):
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have different signs at the interval endpoints.")

    while abs(a-b) >= tolerance:
        midpoint = (a + b) / 2.0
        mid_value = func(midpoint)

        if abs(mid_value) < tolerance:
            return midpoint

        if func(a) * mid_value < 0:
            b = midpoint
        else:
            a = midpoint

    return midpoint

# False Position (Regula Falsi) method
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

# Secant method
def secant_method(func, x0, x1, epsilon=1e-3, max_iterations=1000):
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

# Newton-Raphson method
def newton_raphson(f, df, x0, tol=1e-3, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Apply methods to solve the equation
solution_bisection = bisection_method(equation, -3, 3)
solution_false_position = false_position(equation, -3, 3)
solution_secant = secant_method(equation, -3, 3)
solution_newton_raphson = newton_raphson(equation, derivative_equation, 1)

print(solution_bisection);
print(solution_false_position);
print(solution_secant);
print(solution_newton_raphson);

# Generate data for plotting
x = np.linspace(-3, 3, 400)
y = equation(x)

# Plotting the graph
plt.figure(figsize=(12, 8))
plt.plot(x, y, label="Equation: $x^3 - 5x + 1$")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(solution_bisection, color='red', linestyle='--', label=f'Bisection: x={solution_bisection:}')
plt.axvline(solution_false_position, color='green', linestyle='--', label=f'False Position: x={solution_false_position:}')
plt.axvline(solution_secant, color='blue', linestyle='--', label=f'Secant: x={solution_secant:}')
plt.axvline(solution_newton_raphson, color='purple', linestyle='--', label=f'Newton-Raphson: x={solution_newton_raphson:}')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of $x^3 - 5x + 1 = 0$ with Solutions by Different Methods')
plt.grid(True)
plt.show()
