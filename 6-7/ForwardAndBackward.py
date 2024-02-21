from tabulate import tabulate

def forward_difference(y_vals):
    """
    Compute the forward difference of a list of y values.
    The function returns a list of lists where each sublist represents a higher order difference.
    """
    n = len(y_vals)
    forward_diffs = [y_vals.copy()]
    for order in range(1, n):
        current_diffs = []
        for i in range(n - order):
            current_diffs.append(forward_diffs[order - 1][i + 1] - forward_diffs[order - 1][i])
        forward_diffs.append(current_diffs)
    return forward_diffs

# Step 2: Define the function to calculate backward differences
def backward_difference(y_vals):
    """
    Compute the backward difference of a list of y values.
    The function returns a list of lists where each sublist represents a higher order difference.
    """
    n = len(y_vals)
    backward_diffs = [y_vals.copy()]
    for order in range(1, n):
        current_diffs = []
        for i in range(n):
            current_diffs.append(backward_diffs[order - 1][i] - backward_diffs[order - 1][i-1])
        backward_diffs.append(current_diffs)
    return backward_diffs


def print_diff_table(diffs, title):
    """
    Print the difference table using tabulate for better formatting.
    """
    # Preparing the table with proper alignment
    table = []
    max_len = max(len(diff) for diff in diffs)
    for i in range(max_len):
        row = []
        for diff in diffs:
            try:
                row.append(diff[i])
            except IndexError:
                row.append("")
        table.append(row)
    print(title)
    print(tabulate(table, headers=[f"Order {i}" for i in range(len(diffs))], tablefmt="grid"))


# Sample Data
y_values = [1.1, 2.0, 4.4, 7.9]

# Compute differences
fwd_diffs = forward_difference(y_values)
bwd_diffs = backward_difference(y_values)

print(fwd_diffs);
print(bwd_diffs)