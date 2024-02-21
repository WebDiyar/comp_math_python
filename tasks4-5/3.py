import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'x': np.array([0, 1, 2, 3]),
    'y': np.array([1.05, 2.10, 3.85, 8.30])
}

Y = np.log(data['y'])
X = data['x']


data['log_e'] = np.log(np.e) * X

data['Y'] = Y
data['log_eX'] = data['log_e'] * Y

sum_X = np.sum(X)
sum_Y = np.sum(Y)
sum_log_eX = np.sum(data['log_eX'])
sum_log_e2 = np.sum(data['log_e']**2)

coefficients = np.linalg.solve(
    [[len(X), sum_X], [sum_X, sum_log_e2]],
    [sum_Y, sum_log_eX]
)
A, B = coefficients


a = np.exp(A)
b = B / np.log(np.e)

# Print the table of values
table = pd.DataFrame({
    'x': X,
    'y': data['y'],
    'Y': Y,
    'x^2': X**2,
    'xY': X*Y
})

# Print the table
print("Table of values:")
print(table)

# Print the final equation
print(f"\nThe equation of the curve is: y = {a:.4f} * e^({b:.4f}*x)")

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'], color='blue', label='Original Data')
x_values = np.linspace(0, max(data['x']), 100)
y_values = a * np.exp(b * x_values)
plt.plot(x_values, y_values, color='red', label=f'Curve Fit: y = {a:.4f} * e^({b:.4f}*x)')
plt.title('Curve Fitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

