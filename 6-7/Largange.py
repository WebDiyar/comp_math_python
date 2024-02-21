# Define the Lagrange interpolation function
def lagrange_interpolation(x_values, y_values, x):
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have the same length")
    y = 0

    for i in range(len(x_values)):
        li = 1
        for j in range(len(x_values)):
            if i != j:
                li *= (x - x_values[j]) / (x_values[i] - x_values[j])
        y += y_values[i] * li

    return y

# Given values
# x_values = [5, 6, 9, 11]
# y_values = [12, 13, 14, 16]

x_values = [0, 1, 2, 3, 4]
y_values = [1, 2.7183, 7.3891, 20.0855, 54.5982]

# Calculate the interpolated value for x = 10
x_target = 2.6
y_interpolated = lagrange_interpolation(x_values, y_values, x_target)

# Print the result
print(y_interpolated)