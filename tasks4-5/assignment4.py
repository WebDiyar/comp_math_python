import matplotlib.pyplot as plt
import numpy as np

def power_iteration(A, v, max_iter=1000, tol=1e-5):
    v = np.array(v)
    eigenvalues = []

    for iteration in range(max_iter):
        multiple = np.dot(A, v);
        eigenvalue = np.dot(v, multiple) / np.dot(v, v);

        eigenvalues.append(eigenvalue)

        v = multiple / np.linalg.norm(multiple)

        if len(eigenvalues) > 1 and np.abs(eigenvalues[-1] - eigenvalues[-2]) < tol:
            break

    return eigenvalues

A = [[2, 1], [3, 2]]
v = [3, 2]


eigenvalues = power_iteration(A, v)
print(eigenvalues);
# Plot the convergence of eigenvalues
plt.plot(eigenvalues, marker='x', color='red')
plt.xlabel('Iterations')
plt.ylabel('Eigenvalues')
plt.title('Power Iteration Convergence')
plt.grid(True)
plt.show()
