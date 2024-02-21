# Importing necessary libraries
from sympy import symbols, Function, log

# Define the symbols and function
x = symbols('x')
f = Function('f')(x)

# Define the forward difference operator
def forward_difference(func, at_x):
    delta_x = 1  # Assuming the step for forward difference is 1 for discrete functions
    return func.subs(x, at_x + delta_x) - func.subs(x, at_x)

# Let's define f(x) as a symbolic function which we will use to show the identities
# Note: The actual function f(x) is not given, so we're using the symbolic representation for demonstration

# Identity (i): Δ[1/f(x)] = -Δf(x) / [f(x)f(x+1)]
# We will create a symbolic representation of 1/f(x) and calculate its forward difference
one_over_fx = 1/f
delta_one_over_fx = forward_difference(one_over_fx, x)

# Now we calculate -Δf(x) / [f(x)f(x+1)]
negative_delta_fx_over_fx_squared = -forward_difference(f, x) / (f * f.subs(x, x+1))

# Identity (ii): Δlog(f(x)) = log[1 + Δf(x)/f(x)]
# We will create a symbolic representation of log(f(x)) and calculate its forward difference
log_fx = log(f)
delta_log_fx = forward_difference(log_fx, x)

# Now we calculate log[1 + Δf(x)/f(x)]
log_of_one_plus_delta_fx_over_fx = log(1 + forward_difference(f, x)/f)

# Let's print the results to verify if the identities are satisfied
delta_one_over_fx, negative_delta_fx_over_fx_squared, delta_log_fx, log_of_one_plus_delta_fx_over_fx

print(delta_one_over_fx);
print(negative_delta_fx_over_fx_squared);
print('-------------------------')
print(delta_log_fx);
print(log_of_one_plus_delta_fx_over_fx);