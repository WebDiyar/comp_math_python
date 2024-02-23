import numpy as np

# Define the function f(x) = 1 / (1 + x^2)
def f(x):
    return 1 / (1 + x**2)

# Trapezoidal rule function
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (h/2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])

# Simpson’s 1/3 rule function
def simpson_one_third_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (h/3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[n])

# Simpson’s 3/8 rule function
def simpson_three_eight_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (3 * h / 8) * (y[0] + 3 * np.sum(y[1:-1:3]) + 3 * np.sum(y[2:-1:3]) + 2 * np.sum(y[3:n-1:3]) + y[n])

# Boole’s rule function
def boole_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (2 * h / 45) * (7 * (y[0] + y[n]) + 32 * np.sum(y[1:n:4]) + 12 * np.sum(y[2:n:4]) + 32 * np.sum(y[3:n-1:4]) + 14 * np.sum(y[4:n-2:4]))

# Weddle’s rule function
def weddle_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (3 * h / 10) * (y[0] + 5 * np.sum(y[1:n:6]) + y[n] + 6 * np.sum(y[2:n-1:6]) + y[3] + 5 * np.sum(y[4:n-2:6]) + 2 * np.sum(y[5:n-3:6]))

# Actual value of the integral calculation using arctan
def actual_integral_value(a, b):
    return np.arctan(b) - np.arctan(a)

# Function to calculate all the rules and compare
def calculate_all_rules(a, b, n):
    actual_value = actual_integral_value(a, b)
    trap_rule = trapezoidal_rule(a, b, n)
    simp_1_3_rule = simpson_one_third_rule(a, b, n)
    simp_3_8_rule = simpson_three_eight_rule(a, b, n)
    boole_rule_val = boole_rule(a, b, n)
    weddle_rule_val = weddle_rule(a, b, n)

    return {
        "actual_value": actual_value,
        "trapezoidal_rule": trap_rule,
        "simpson_1_3_rule": simp_1_3_rule,
        "simpson_3_8_rule": simp_3_8_rule,
        "boole_rule": boole_rule_val,
        "weddle_rule": weddle_rule_val
    }

# Define the interval [a, b] and the number of sub-intervals n
a = 0
b = 6
n = 6

# Calculate and output the results
results = calculate_all_rules(a, b, n)
for rule, value in results.items():
    print(f"{rule}: {value}")
