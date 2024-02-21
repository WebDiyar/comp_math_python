import numpy as np

x_values = np.array([110, 130, 160, 190])
y_values = np.array([10.8, 8.1, 5.5, 4.8])

# Lagrange's interpolation formula
def lagrange_interpolation(x, y, target):
    result = 0.0
    for i in range(len(y)):
        terms = 1.0
        for j in range(len(x)):
            if i != j:
                terms *= (target - x[j]) / (x[i] - x[j])
        result += terms * y[i]
    return result

viscosity_at_140 = lagrange_interpolation(x_values, y_values, 140)

print(viscosity_at_140);