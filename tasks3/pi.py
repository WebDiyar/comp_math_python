import math
import matplotlib.pyplot as plt
import numpy as np


radius = 6

Pi1 = math.pi
Pi2 = 3.14

area_Pi1 = Pi1 * radius**2
area_Pi2 = Pi2 * radius**2

absolute_error = abs(area_Pi1 - area_Pi2)
relative_error = absolute_error / area_Pi1
percentage_error = relative_error * 100

print(area_Pi1);
print(area_Pi2);
print(absolute_error);
print(relative_error);
print(percentage_error);




fig, ax = plt.subplots()

circle_exact = plt.Circle((0, 0), np.sqrt(Pi1 / np.pi), color='blue', fill=False, label='Exact')

circle_approx = plt.Circle((0, 0), np.sqrt(Pi2 / np.pi), color='green', fill=False, linestyle='--', label='Approx')

ax.add_patch(circle_exact)
ax.add_patch(circle_approx)

ax.set_aspect('equal')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.legend()

plt.show()