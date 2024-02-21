def f(x):
    return x**3 + 5*x - 7

x_values = [-1, 0, 1, 2, 3, 4, 5]
f_values = [f(x) for x in x_values]

def differences(values):
    return [values[i+1] - values[i] for i in range(len(values) - 1)]

first_order_diff = differences(f_values)
second_order_diff = differences(first_order_diff)
third_order_diff = differences(second_order_diff)

# Since the function is a cubic one, we expect constant third-order differences.
# We can use this constant third-order difference to predict f(6).
# The difference to get f(6) will be the last second-order difference plus the third-order difference.
predicted_second_order_diff = second_order_diff[-1] + third_order_diff[-1]

# Now we add this predicted second-order difference to the last first-order difference to get the
# predicted first-order difference for f(6).
predicted_first_order_diff = first_order_diff[-1] + predicted_second_order_diff

# Finally, we add the predicted first-order difference to f(5) to get f(6).
predicted_f_6 = f_values[-1] + predicted_first_order_diff

print(predicted_f_6);
print(f_values);
print(first_order_diff);
print(second_order_diff);
print(third_order_diff);