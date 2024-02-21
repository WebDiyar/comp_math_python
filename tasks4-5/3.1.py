import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x_exp = np.array([0, 1, 2, 3])
y_exp = np.array([1.05, 2.10, 3.85, 8.30])

def exponential_curve(x, a, b):
    return a * np.exp(b * x)

params, covariance = curve_fit(exponential_curve, x_exp, y_exp)

a, b = params

a_approx = round(a, 1)
b_approx = round(b, 1)

x_dense_exp = np.linspace(min(x_exp), max(x_exp), 200)
y_dense_exp = exponential_curve(x_dense_exp, a, b)

def analytical_exponential_curve(x, a, b):
    return a * np.exp(b * x)

y_analytical_exp = analytical_exponential_curve(x_dense_exp, a_approx, b_approx)

plt.scatter(x_exp, y_exp, label='Data points')
plt.plot(x_dense_exp, y_dense_exp, label=f'Fitted curve y = {a_approx:.1f}e^({b_approx:.1f}x)', color='blue', linestyle='--')
plt.plot(x_dense_exp, y_analytical_exp, label=f'Analytical curve y = {a_approx:.1f}e^({b_approx:.1f}x)', color='red', linestyle='--')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Fit')
plt.legend()
plt.grid(True)
plt.show()
print(a,b)
print(a_approx, b_approx)
