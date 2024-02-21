import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

# functions
def f1(x):
    return x**2 + 4*np.sin(x)

def df1(x):
    return 2*x + 4 * np.cos(x)

def f2(x):
    return np.cos(x) - x*np.exp(x)

def df2(x):
    return -np.sin(x) - np.exp(x) - x * np.exp(x)

# Newton-Raphson method
def newton_raphson(f, df, x0, tol=1e-3, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x) # end guesses
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Initial start guesses
x0_1 = -4
x0_2 = 0.5

# Apply Newton-Raphson method
root1 = newton_raphson(f1, df1, x0_1)
root2 = newton_raphson(f2, df2, x0_2)

# Plotting
x_values = np.linspace(-3, 3, 400)
plt.figure(figsize=(10, 6))
plt.plot(x_values, f1(x_values), label='x^2 + 4*sin(x)')
plt.plot(x_values, f2(x_values), label='cos(x) - x*e^x')
plt.axhline(0, color='black',linewidth=0.5)
plt.scatter([root1, root2], [f1(root1), f2(root2)], color='red')
plt.title('Graphs of the Functions and Their Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

print(root1);
print(root2);
