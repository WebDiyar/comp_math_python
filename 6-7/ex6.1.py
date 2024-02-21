def forward_difference(y_values):
    """
    Compute the first order forward difference of a list of y values.

    Parameters:
    y_values (list): A list of y values for which the forward differences are to be computed.

    Returns:
    list: A list of first order forward differences.
    """
    return [y_values[i + 1] - y_values[i] for i in range(len(y_values) - 1)]


# Next, I will create a function that computes all orders of forward differences and
# organizes them into a structure that can be easily used to print a forward difference table.

def compute_all_forward_differences(x_values, y_values):
    """
    Compute all orders of forward differences for a given set of x and y values.

    Parameters:
    x_values (list): A list of x values.
    y_values (list): A list of y values.

    Returns:
    dict: A dictionary where keys are the order of the difference (1st, 2nd, etc.),
          and values are lists of differences of that order.
    """
    # Initialize the dictionary with the 0th order differences (the y values themselves)
    differences = {'0th': y_values.copy()}

    # We start with the first order differences
    current_order_differences = y_values
    order = 0

    # We compute differences until we have only one value left
    while len(current_order_differences) > 1:
        current_order_differences = forward_difference(current_order_differences)
        order += 1
        differences[f'{order}th'] = current_order_differences

    return differences


# Now, let's write a function that will print the table using the computed differences.

def print_forward_difference_table(x_values, differences):
    """
    Print the forward difference table.

    Parameters:
    x_values (list): A list of x values.
    differences (dict): A dictionary of forward differences.
    """
    # Calculate the width of the column based on the longest x value
    column_width = max(len(str(x)) for x in x_values) + 4

    # Print the header
    print(f"{'x':^{column_width}}", end="")
    for order in differences:
        if order == '0th':
            print(f"{'y':^{column_width}}", end="")
        else:
            print(f"{order} diff".center(column_width), end="")
    print()

    # Print the rows
    for i in range(len(x_values)):
        # Print the x value
        print(f"{x_values[i]:^{column_width}}", end="")

        # Print the y and difference values for each order
        for order in differences:
            if i < len(differences[order]):
                print(f"{differences[order][i]:^{column_width}.2f}", end="")
            else:
                print(" " * column_width, end="")
        print()

# We will comment out the actual function calls for now to comply with the instructions.

# Define the x and y values as given in the problem
x_values = [10, 20, 30, 40]
y_values = [1.1, 2.0, 4.4, 7.9]

# Compute all forward differences
differences = compute_all_forward_differences(x_values, y_values)

# Print the forward difference table
print_forward_difference_table(x_values, differences)

