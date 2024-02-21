import numpy as np
import matplotlib.pyplot as plt

# functions
def f(x):
    return x**3 - x - 1

# def f2(x):
#     return x - np.cos(x)
#
# def f3(x):
#     return np.exp(-x) - x

# bisection method
# def bisection_method(func, a, b, tolerance=1e-3, iteration):
#     if func(a) * func(b) >= 0:
#         raise ValueError("Function must have different signs at the interval endpoints.")
#
#     while abs(a-b) >= tolerance:
#         midpoint = (a + b) / 2.0
#         mid_value = func(midpoint)
#
#         if abs(mid_value) < tolerance:
#             return midpoint
#
#         if func(a) * mid_value < 0:
#             b = midpoint
#         else:
#             a = midpoint
#
#     return midpoint


def bisection_method(a, b, tol=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    A = a
    B = b
    for n in range(1, max_iterations):
        C = (A + B) / 2
        if abs(f(C)) < tol:
            return C, n
        elif f(A) * f(C) < 0:
            B = C
        elif f(B) * f(C) < 0:
            A = C
    return C, n



# Applying the custom Bisection method
root1_custom = bisection_method(f, 1, 2)
root2_custom = bisection_method(f2, 0, 1)
root3_custom = bisection_method(f3, 0, 1)

print(root1_custom);
print(root2_custom);
print(root3_custom);


# # Redefining the range for x values
# x_values = np.linspace(-2, 2, 400)
# f1_values = f1(x_values)
# f2_values = f2(x_values)
# f3_values = f3(x_values)
#
# # Plotting
# plt.figure(figsize=(10, 6))
# plt.plot(x_values, f1_values, label='f(x) = x^3 - x - 1')
# plt.plot(x_values, f2_values, label='f(x) = x - cos(x)')
# plt.plot(x_values, f3_values, label='f(x) = e^(-x) - x')
# plt.axhline(0, color='black',linewidth=0.5)
# plt.axvline(root1_custom, color='b', linestyle='--', label=f'Root 1: {root1_custom:}')
# plt.axvline(root2_custom, color='r', linestyle='--', label=f'Root 2: {root2_custom:}')
# plt.axvline(root3_custom, color='g', linestyle='--', label=f'Root 3: {root3_custom:}')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Graphs of Functions and their Roots using Custom Bisection Method')
# plt.grid(True)
# plt.show()
