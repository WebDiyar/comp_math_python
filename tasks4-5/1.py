import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 1.8, 1.3, 2, 6.3])

u = x - 2

sum_u = np.sum(u)
sum_u2 = np.sum(u**2)
sum_u3 = np.sum(u**3)
sum_u4 = np.sum(u**4)
sum_y = np.sum(y)
sum_yu = np.sum(y * u)
sum_yu2 = np.sum(y * u**2)

# Coefficients for the normal equations
coefficients = np.array([
    [len(x), sum_u, sum_u2],
    [sum_u, sum_u2, sum_u3],
    [sum_u2, sum_u3, sum_u4]
])

# Constants on the right hand side of the equations
constants = np.array([sum_y, sum_yu, sum_yu2])

# Solving for A, B, C
A, B, C = np.linalg.solve(coefficients, constants)

print(f"A = {A}, B = {B}, C = {C}")

def parabola(x):
    return A + B*(x - 2) + C*(x - 2)**2

# Generate a range of x values for plotting the parabola
x_values = np.linspace(min(x), max(x), 400)
y_values = parabola(x_values)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Data points')
plt.plot(x_values, y_values, label=f'Fitted parabola: y = {A:.2f} - {B:.2f}*(x - 2) + {C:.2f}*(x - 2)^2')
plt.title('Fit a second degree parabola to the data')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
