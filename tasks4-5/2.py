import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'x': [6, 7, 7, 8, 8, 8, 9, 9, 10],
    'y': [5, 5, 4, 5, 4, 3, 4, 3, 3]
}

# Creating a DataFrame from the data
df = pd.DataFrame(data)

# Calculating additional necessary columns for the normal equations
df['xy'] = df['x'] * df['y']
df['x^2'] = df['x'] ** 2

# Summations needed for the equations
sum_x = df['x'].sum()
sum_y = df['y'].sum()
sum_xy = df['xy'].sum()
sum_x2 = df['x^2'].sum()

# Number of data points
n = len(df)

# Calculating the coefficients a and b for the line y = ax + b
# Based on the normal equations for least squares fitting
A = np.array([[sum_x2, sum_x], [sum_x, n]])
b = np.array([sum_xy, sum_y])

# Solving for a and b
coefficients = np.linalg.solve(A, b)
a, b = coefficients

# Printing the table
print("Table of values:")
print(df)

# Printing the equation of the line
print(f"\nThe equation of the line is: y = {a:.1f}x + {b:.1f}")

# Plotting the data points
plt.scatter(df['x'], df['y'], color='red', label='Data points')

# Plotting the line of best fit
x_values = np.linspace(min(df['x']), max(df['x']), 100)
y_values = a * x_values + b
plt.plot(x_values, y_values, label=f'Best fit line: y = {a:.1f}x + {b:.1f}')

# Setting up plot labels
plt.title('Line of Best Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
