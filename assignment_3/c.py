import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients of the system of equations
A = np.array([[5, -1, 1],
              [2, 4, 0],
              [1, 1, 5]], dtype=float)

# Define the constants of the system of equations
b = np.array([10, 12, -1], dtype=float)

# Initial guess for the solution
x0 = np.array([2, 3, 0], dtype=float)

# Maximum number of iterations
max_iterations = 100

# Tolerance for the stopping criterion
tolerance = 1e-10

# Implementation of Jacobi's Method with tracking of iterations
def jacobi_with_tracking(A, b, x0, tolerance, max_iterations):
    D = np.diag(A)  # Diagonal elements of A
    R = A - np.diagflat(D)  # Remainder of A after removing the diagonal

    x = x0
    iteration_values = [x0]  # List to store the values of x at each iteration

    for i in range(max_iterations):
        x_new = (b - np.dot(R, x)) / D
        iteration_values.append(x_new)
        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new, iteration_values
        x = x_new
    return x, iteration_values

# Solve the system using Jacobi's method and track the iterations
solution, iteration_values = jacobi_with_tracking(A, b, x0, tolerance, max_iterations)
rounded_solution = [round(x, 3) for x in solution]
print(rounded_solution)

# Plotting the results
iterations = range(len(iteration_values))
values = np.array(iteration_values)

# Plot for each variable
plt.plot(iterations, values[:, 0], label='X')
plt.plot(iterations, values[:, 1], label='Y')
plt.plot(iterations, values[:, 2], label='Z')

plt.xlabel('Iteration')
plt.ylabel('Values')
plt.title('Jacobi Method Iteration Values')
plt.legend();
plt.show();
