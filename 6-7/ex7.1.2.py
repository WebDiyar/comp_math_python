import numpy as np

# Data points from the table
x_points = np.array([1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3])
y_points = np.array([5.474, 6.050, 6.686, 7.389, 8.166, 9.025, 9.974])


# Function to calculate the divided differences table
def divided_difference(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef


# Function to apply Newton's Interpolation Formula
def newtons_interpolation(x, y, value):
    coef = divided_difference(x, y)[0, :]
    n = len(coef) - 1
    result = coef[n]

    for i in range(n - 1, -1, -1):
        result = result * (value - x[i]) + coef[i]

    return result


# Applying Newton's Interpolation for x = 1.85 and x = 2.4
y_185 = newtons_interpolation(x_points, y_points, 1.85)
y_24 = newtons_interpolation(x_points, y_points, 2.4)

# Since we want specific formatting for the output, we'll round the results
y_185_rounded = round(y_185, 2)
y_24_rounded = round(y_24, 2)

print(y_185_rounded);
print(y_24_rounded)