import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def jacobi_method(A, b, tolerance=1e-5, max_iterations=1000):
    """
    Solves the system of linear equations Ax = b using Jacobi's iterative method.

    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :param tolerance: Tolerance for convergence
    :param max_iterations: Maximum number of iterations
    :return: Solution vector, iteration history
    """
    # Initialization
    x = np.zeros_like(b, dtype=np.double)
    D = np.diag(A)
    R = A - np.diagflat(D)

    # Iteration History
    history = []

    # Iterative algorithm
    for i in range(max_iterations):
        x_new = (b - np.dot(R, x)) / D
        history.append(x_new.copy())

        # Compute error
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            break

        x = x_new

    return x, np.array(history)


# Coefficient matrix A and right-hand side vector b
A = np.array([[5, 2, 1], [-1, 4, 2], [2, -3, 10]])
b = np.array([7, 3, -1])

# Solve using Jacobi's method
solution, history = jacobi_method(A, b)

# Create a table for iteration history
iterations = np.arange(len(history)) + 1  # Iteration numbers
errors = np.vstack((np.zeros(3), np.abs(np.diff(history, axis=0))))  # Error calculation

table = pd.DataFrame(np.hstack((iterations[:, None], history, errors)),
                     columns=["N", "X", "Y", "Z", "Error_X", "Error_Y", "Error_Z"])

solution, table.head(15)  # Display solution and the first 10 rows of the table

print(solution);
print(table.head(20));


# Extracting X, Y, and Z values from the history
X_values = history[:, 0]
Y_values = history[:, 1]
Z_values = history[:, 2]
iterations = np.arange(1, len(history) + 1)

# Plotting the graphs
plt.figure(figsize=(15, 5))

# Graph for X
plt.subplot(1, 3, 1)
plt.plot(iterations, X_values, marker='o', linestyle='-')
plt.title("X values per Iteration")
plt.xlabel("Iteration")
plt.ylabel("X Value")
plt.grid(True)

# Graph for Y
plt.subplot(1, 3, 2)
plt.plot(iterations, Y_values, marker='o', color='orange', linestyle='-')
plt.title("Y values per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Y Value")
plt.grid(True)

# Graph for Z
plt.subplot(1, 3, 3)
plt.plot(iterations, Z_values, marker='o', color='green', linestyle='-')
plt.title("Z values per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Z Value")
plt.grid(True)

# Displaying the plots
plt.tight_layout()
plt.show()
