# Define the given data points
x = [1, 1.4, 1.8, 2.2]
f_x = [3.49, 4.82, 5.96, 6.5]

# Calculate the step size (h)
h = x[1] - x[0]

# Initialize the difference table with the given f(x) values
difference_table = [f_x]

# Calculate the finite differences
for level in range(1, len(x)):
    differences = []
    for i in range(len(difference_table[level-1]) - 1):
        diff = difference_table[level-1][i+1] - difference_table[level-1][i]
        differences.append(diff)
    difference_table.append(differences)

# Define the function to calculate the factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Define the function to calculate the value using Newton's forward formula
def newtons_forward_formula(x_value, x, difference_table, h):
    # Calculate 'u' used in the formula
    u = (x_value - x[0]) / h

    # Initialize result with the first term of the difference table
    result = difference_table[0][0]

    # Loop to calculate each term and add it to the result
    for i in range(1, len(x)):
        u_term = 1
        for j in range(i):
            u_term *= (u - j)
        result += (u_term * difference_table[i][0]) / factorial(i)

    return result

# Calculate the value at x = 1.6
value_at_1_6 = newtons_forward_formula(1.6, x, difference_table, h)

print(value_at_1_6);
