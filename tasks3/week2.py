import numpy as np
import matplotlib.pyplot as plt

#function
def f(x):
    return x**3 - x - 1


# 0=-1
# 2=5

# Bisection Method
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

# Secant Method
def secant_method(a, b, tol=1e-6, max_iterations=100):
    for n in range(max_iterations):
        if abs(f(a) - f(b)) < tol:
            return b, n
        c = b - f(b) * (b - a) / (f(b) - f(a))
        #0, 0.3, 2 - a c b
        a = b
        b = c
        if abs(f(c)) < tol:
            return c, n
    return c, n

# Method of False Position
def false_position_method(a, b, tol=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("False position method fails.")
        return None
    for n in range(max_iterations):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c, n
        if f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c
    return c, n

# Initial guesses for each method
a_bisec, b_bisec = 1, 2  # Initial interval for bisection
a_sec, b_sec = 0, 2      # Initial guesses for secant
a_false, b_false = 0, 2  # Initial interval for false position

# Solving using each method
root_bisection, iter_bisection = bisection_method(a_bisec, b_bisec)
root_secant, iter_secant = secant_method(a_sec, b_sec)
root_false_position, iter_false = false_position_method(a_false, b_false)

print('Bisection: ', root_bisection, iter_bisection);
print('Secant: ', root_secant, iter_secant);
print('False_Position: ', root_false_position, iter_false)

#----------------------------------------------------------------------------------------------
x_values = np.linspace(0, 2, 400)
y_values = f(x_values)

# Plotting the function
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="f(x) = x^3 - x - 1", color='blue')

# Marking the roots found by each method
plt.scatter(root_bisection, f(root_bisection), color='red', label=f"Bisection Root: {root_bisection:.6f}")
plt.scatter(root_secant, f(root_secant), color='green', label=f"Secant Root: {root_secant:.6f}")
plt.scatter(root_false_position, f(root_false_position), color='orange', label=f"False Position Root: {root_false_position:.6f}")

# Adding labels and legend
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Convergence of Bisection, Secant, and False Position Methods")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
