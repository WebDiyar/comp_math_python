u = [3, 12, 81, 2000, 100]

# Function to calculate the nth forward difference
def forward_difference(u, n):
    for _ in range(n):
        u = [j-i for i, j in zip(u[:-1], u[1:])]
    return u[0]

# Calculate the 4th forward difference
delta4_u0 = forward_difference(u, 4)
print(delta4_u0)


