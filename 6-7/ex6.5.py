# Step 1: Define the function f(x)
def f(x):
    return x**3 + x**2 - 2*x + 1

# Step 2: Compute the values of f(x) for x = 0, 1, 2, 3, 4, 5
x_values = list(range(7))  # Including 6 for direct calculation later
y_values = [f(x) for x in x_values]

# Step 3: Create a difference table
# The difference table will be a list of lists, where the first list is the y_values
# and each subsequent list is the difference between the previous list's elements
difference_table = [y_values]
for level in range(1, len(y_values)):
    differences = [j - i for i, j in zip(difference_table[level - 1][:-1], difference_table[level - 1][1:])]
    difference_table.append(differences)

# Since we need to predict for x=6, we need to add another level of differences by extending the table
# We will keep the last difference constant as it's a cubic polynomial and extend the table
last_difference = difference_table[-1][0]
difference_table[-1].append(last_difference)
for level in range(len(y_values) - 2, 0, -1):
    next_value = difference_table[level][-1] + difference_table[level - 1][-1]
    difference_table[level - 1].append(next_value)

# Step 4: The value of f(x) for x=6 is now the last element in the first list of the difference table
predicted_value = difference_table[0][-1]

# Step 5: Verify the predicted value by directly substituting x=6 into the function f(x)
verification_value = f(6)


print(difference_table);
print(predicted_value);
print(verification_value);