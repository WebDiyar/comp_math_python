import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Given data points
x_values = np.array([0, 1, 2, 3, 4, 5])
y_values = np.array([4, 8, 15, 7, 6, 2])

# Fit a polynomial to the data points
degree = len(x_values) - 1  # The degree of the polynomial
coefs = Polynomial.fit(x_values, y_values, degree).convert().coef

# Create a Polynomial object from the coefficients
p = Polynomial(coefs)

# Differentiate the polynomial to get the first and second derivatives
dp = p.deriv(1)
d2p = p.deriv(2)

# Calculate the second derivative at x = 0
y_at_0 = p(0)
d2y_at_0 = d2p(0)

# Output the results
print(f"The value of y(0) is: {y_at_0}")
print(f"The value of y''(0) is: {d2y_at_0}")
