import numpy as np
import pandas as pd

# Given data
x = np.array([0, 1, 2, 3, 4])
f_x = np.array([1, 2.7183, 7.3891, 20.0855, 54.5982])
n = len(x)
h = x[1] - x[0]  # Assuming uniform spacing

# Calculate forward differences
forward_diff = np.zeros((n, n))
forward_diff[:, 0] = f_x
for i in range(1, n):
    for j in range(n-i):
        forward_diff[j, i] = forward_diff[j+1, i-1] - forward_diff[j, i-1]

# Calculate backward differences
backward_diff = np.zeros((n, n))
backward_diff[:, 0] = f_x
for i in range(1, n):
    for j in range(n-1, i-1, -1):
        backward_diff[j, i] = backward_diff[j, i-1] - backward_diff[j-1, i-1]

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Interpolation function for Newton's Forward and Backward
def newton_forward_backward(x, x_data, forward_diff, backward_diff, h, value):
    # Forward
    s = (value - x_data[0]) / h
    forward_sum = forward_diff[0, 0]
    for i in range(1, len(x)):
        term = forward_diff[0, i]
        for j in range(i):
            term *= (s - j)
        term /= factorial(i)
        forward_sum += term

    # Backward
    s = (value - x_data[-1]) / h
    backward_sum = backward_diff[-1, 0]
    for i in range(1, len(x)):
        term = backward_diff[-1, i]
        for j in range(i):
            term *= (s + j)
        term /= factorial(i)
        backward_sum += term

    return forward_sum, backward_sum

# Interpolate value at x = 2.5
value = 2.6
forward_estimate, backward_estimate = newton_forward_backward(x, x, forward_diff, backward_diff, h, value)

forward_diff_table = pd.DataFrame(forward_diff).iloc[:, :5]
backward_diff_table = pd.DataFrame(backward_diff).iloc[:, :5]


print(forward_diff_table);
print(backward_diff_table);
print(forward_estimate);
print(backward_estimate)