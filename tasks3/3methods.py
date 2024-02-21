import matplotlib.pyplot as plt

def f(x):
    return x ** 3 - x - 1

# Bisection method
def bisection(a, b, epsilon):
    i = 1
    roots = []
    iteration = []
    while abs(a - b) >= epsilon:
        iteration.append(i)
        i += 1
        x = (a + b) / 2
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        roots.append(x)
    return roots, iteration

# Secant method
def secant_method(x0, x1, epsilon):
    roots = []
    iteration = []
    i = 1
    while abs(a - b) >= epsilon:
        iteration.append(i)
        i += 1
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        roots.append(x2)
        if abs(x2 - x1) < epsilon:
            break
        x0, x1 = x1, x2
    return roots, iteration



def false_position(a, b, epsilon):
    roots = []
    iteration = []
    x_values = []

    i = 1
    x2 = a  # Initialize x2 with 'a'
    x0 = b  # Initialize x0 with 'b'

    while abs(a - b) >= epsilon:
        iteration.append(i)

        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        roots.append(x)
        x_values.append((a, b, x))  # Store 'a', 'b', and 'x' values at each iteration

        if abs(f(x)) < epsilon or abs(x2 - x0) < epsilon:
            break

        if f(x) * f(a) < 0:
            b = x
        else:
            a = x
        
        i += 1

    return roots, iteration


# Define parameters
a = 1
b = 2
epsilon = 10 ** -4

# Bisection method
roots_bisection, iter_bisection = bisection(a, b, epsilon)
print(roots_bisection, iter_bisection)
plt.plot(iter_bisection, roots_bisection, marker='o', label='Bisection')

# Secant method
roots_secant, iter_secant = secant_method(a, b, epsilon)
print(roots_secant, iter_secant);
plt.plot(iter_secant, roots_secant, marker='o', label='Secant')

# False Position method
roots_false_position, iter_false_position = false_position(a, b, epsilon)
print(roots_false_position, iter_false_position);
plt.plot(iter_false_position, roots_false_position, marker='o', label='False Position')

plt.xlabel('Iteration')
plt.ylabel('Root Estimate')
plt.title('Root Finding Methods')
plt.legend()
plt.show()
