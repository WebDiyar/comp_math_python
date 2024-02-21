import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gauss_jordan_improved(A, b):
    # Improved Gauss-Jordan Method
    n = len(A)
    m = len(A[0])

    # Check if the system is underdetermined (more variables than equations)
    if m > n:
        return "The system is underdetermined. It may have infinitely many solutions or no solutions."

    # Convert numpy arrays to regular Python lists
    A = A.tolist()
    b = b.tolist()

    M = [row[:] for row in A]  # Clone the matrix to avoid modifying the original

    # Append the constant terms to the matrix
    for i in range(n):
        M[i].append(b[i])

    # Perform row operations
    for k in range(n):
        # Find the pivot
        max_row_index = max(range(k, n), key=lambda i: abs(M[i][k]))
        M[k], M[max_row_index] = M[max_row_index], M[k]

        # Check for zero pivot (singular matrix)
        if M[k][k] == 0:
            return "No unique solution exists for this system."

        # Eliminate entries below the pivot
        for i in range(k + 1, n):
            factor = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= factor * M[k][j]

    # Back substitution
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = M[i][n] / M[i][i]
        for j in range(i):
            M[j][n] -= M[j][i] * x[i]

    return x

# Test the improved function with both systems
A1 = np.array([[2, 5, 7], [2, 1, -1], [1, 1, 1]], dtype=float)
b1 = np.array([52, 0, 9], dtype=float)

result1 = gauss_jordan_improved(A1, b1)

A2 = np.array([[2, 1, 5, 1], [1, 1, -3, 4]], dtype=float);
b2 = np.array([5, -1], dtype=float);
result2 = gauss_jordan_improved(A2, b2)

print("Result of (i): ", result1)
print("Result of (ii): ", result2)


# Solution obtained from the Gauss-Jordan method
solution1 = np.array(result1)

# Create a meshgrid for plotting
x_values = np.linspace(-10, 10, 100)
y_values = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x_values, y_values)

# Extract coefficients
a, b, c = A1[:,0], A1[:,1], A1[:,2]

# Calculate z values for each plane
z1 = (b1[0] - a[0]*x - b[0]*y) / c[0]
z2 = (b1[1] - a[1]*x - b[1]*y) / c[1]
z3 = (b1[2] - a[2]*x - b[2]*y) / c[2]

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the planes
ax.plot_surface(x, y, z1, alpha=0.5, rstride=100, cstride=100)
ax.plot_surface(x, y, z2, alpha=0.5, rstride=100, cstride=100, color='red')
ax.plot_surface(x, y, z3, alpha=0.5, rstride=100, cstride=100, color='green')

# Plot the solution point
ax.scatter(solution1[0], solution1[1], solution1[2], color='black', s=100)

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Graphical Representation of the System of Equations')

# Show the plot
plt.show()