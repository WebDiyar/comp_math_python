import numpy as np


# Define the differential equation as a function
def f(x, y):
    return (y - x) / (y + x)


# Define Picard's iterative method
def picard_method(x0, y0, x, n_iter=5):
    # Initial approximation of y
    y_prev = y0

    for i in range(n_iter):
        # Define the integrand using the previous approximation of y
        integrand = lambda xi: f(xi, y_prev + (xi - x0) * (y_prev - y0) / (x0 - x))

        # Integrate using numerical integration (trapezoidal rule)
        x_values = np.linspace(x0, x, 100)
        y_values = [integrand(xi) for xi in x_values]
        y_next = y0 + np.trapz(y_values, x_values)

        # Update the approximation
        y_prev = y_next

    return y_next


# Initial conditions
x0 = 0
y0 = 1

# Point at which we want to find the value of y
x = 0.1

# Use Picard's method to approximate y(0.1)
y_approx = picard_method(x0, y0, x)
print(y_approx)
