def gauss_elimination(A, b):
    n = len(A)

    # Perform Gauss elimination
    for i in range(n):
        # Find the pivot element
        pivot = abs(A[i][i])
        pivot_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > pivot:
                pivot = abs(A[j][i])
                pivot_row = j

        # Swap the pivot row with the current row (if necessary)
        if pivot_row != i:
            A[i], A[pivot_row] = A[pivot_row], A[i]
            b[i], b[pivot_row] = b[pivot_row], b[i]

        # Eliminate the current variable from the other equations
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Back-substitute to find the solution
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] = round(x[i] / A[i][i], 1)  # Round to 1 decimal place

    return x

# A - Coefficient Matrix
A = [[1, 1, 1],
     [2, -3, 4],
     [3, 4, 5]]
b = [9, 13, 40]

# Solve the system of equations
x = gauss_elimination(A, b)
print("Solution:", x)
