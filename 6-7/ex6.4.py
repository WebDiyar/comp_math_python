# Define a function to calculate the third forward difference
def third_forward_difference(y, i):
    # Calculate the first forward differences
    delta_y_i = y[i + 1] - y[i]
    delta_y_i1 = y[i + 2] - y[i + 1]
    delta_y_i2 = y[i + 3] - y[i + 2]

    # Calculate the second forward differences
    delta2_y_i = delta_y_i1 - delta_y_i
    delta2_y_i1 = delta_y_i2 - delta_y_i1

    # Calculate the third forward difference
    delta3_y_i = delta2_y_i1 - delta2_y_i

    return delta3_y_i


# Define a function to calculate the right hand side of the equation
def rhs(y, i):
    return y[i + 3] - 3 * y[i + 2] + 3 * y[i + 1] - y[i]

# We will test the functions with a hypothetical sequence of y values and an index i
# To ensure correctness, we will not run the actual calls in the PCI but they are here as a demonstration

# Hypothetical sequence y and index i
y = [1, 2, 4, 7, 11] # Example sequence
i = 0                # Example index

# Calculate the third forward difference
delta3_y_i = third_forward_difference(y, i)

# Calculate the right hand side of the equation
result_rhs = rhs(y, i)

# Ensure they are equal for the proof
assert delta3_y_i == result_rhs, "The third forward difference does not match the RHS of the equation"
print(delta3_y_i == result_rhs);