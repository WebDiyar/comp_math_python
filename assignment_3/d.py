import numpy as np

def is_diagonally_dominant(A):
    D = np.diag(np.abs(A))  # Diagonal elements
    S = np.sum(np.abs(A), axis=1) - D  # Sum of non-diagonal elements by row
    return np.all(D >= S)

# Gauss-Seidel method
def gauss_seidel(A, b, x, iterations):
    n = len(A)
    for _ in range(iterations):
        for j in range(n):
            d = b[j]
            for i in range(n):
                if j != i:
                    d -= A[j][i] * x[i]
            x[j] = d / A[j][j]
    return x

# Given matrices
A_GS = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]])
b_GS = np.array([12, 13, 14])
initial_guess = np.zeros(len(b_GS))

# Check if the matrix is diagonally dominant
diagonal_dominance = is_diagonally_dominant(A_GS)


if diagonal_dominance:
    solution = gauss_seidel(A_GS, b_GS, initial_guess, 1000);
    solution = solution.tolist()
else:
    solution = None

print(solution);