import numpy as np

x_log_values = np.array([654, 658, 659, 661])
y_log_values = np.array([2.8156, 2.8182, 2.8189, 2.8202])

def lagrange_interpolation(x, y, target):
    result = 0.0
    for i in range(len(y)):
        terms = 1.0
        for j in range(len(x)):
            if i != j:
                terms *= (target - x[j]) / (x[i] - x[j])
        result += terms * y[i]
    return result

log_at_656 = lagrange_interpolation(x_log_values, y_log_values, 656)
print(log_at_656);
