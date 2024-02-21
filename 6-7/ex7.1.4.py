import numpy as np

# Given values
angles = np.array([45, 50, 55, 60])  # degrees
sine_values = np.array([0.7071, 0.7660, 0.8192, 0.8660])

# Step size (h)
h = 5  # degrees

# Target value (p)
p = (52 - angles[0]) / h

# Calculate the forward differences
forward_diff = np.zeros((len(sine_values), len(sine_values)))
forward_diff[:, 0] = sine_values

for i in range(1, len(sine_values)):
    for j in range(len(sine_values) - i):
        forward_diff[j][i] = forward_diff[j + 1][i - 1] - forward_diff[j][i - 1]

# Applying Newton's Forward Formula
sin_52 = sine_values[0]
s_fact = p
for i in range(1, len(sine_values)):
    sin_52 += (s_fact * forward_diff[0][i]) / np.math.factorial(i)
    s_fact *= (p - i)

# The result should be rounded to four decimal places as per the given values' precision
sin_52 = round(sin_52, 4)

print(sin_52);

