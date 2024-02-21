import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([1.8, 5.1, 8.9, 14.1, 19.8])

# We want to fit a model y = ax + bx^2. This can be done by setting up a linear system to solve for a and b.
# The system is obtained by partial derivatives of the least squares error function with respect to a and b,
# which gives us two equations (normal equations):

# [Σx^2, Σx^3] [a] = [Σxy]
# [Σx^3, Σx^4] [b]   [Σx^2y]

# We'll set this up using matrices and solve for [a, b].

X = np.vstack((x, x**2)).T
A = np.dot(X.T, X)
B = np.dot(X.T, y)


coeffs = np.linalg.solve(A, B)
a, b = coeffs

y_fitted = a*x + b*x**2

# Plot
plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='red', label='Original data')
plt.plot(x, y_fitted, label=f'Fitted curve y = {a:.2f}x + {b:.2f}x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Fit to the curve y = ax + bx^2')
plt.legend()
plt.grid(True)
plt.show()

print(a);
print(b);
