# %% markdown
# # Physics with Python
# We will use Python to solve physics problems. Don't be afraid of the code, it is very simple and easy to understand.
# secondly we can use GPT to explain and modify the code.

# %% codecell
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


# %% codecell
# Example 1: Projectile Motion
# Let's solve a simple projectile motion problem
# A projectile is launched with a velocity of 20 m/s at an angle of 30 degrees.
# How far will it travel in the horizontal direction?
# Let's solve this problem using Python

# Constants
v = 20  # m/s
theta = 30  # degrees
g = 9.81  # m/s^2

# Convert angle to radians
theta = np.radians(theta)

# Calculate horizontal distance
d = (v**2 * np.sin(2 * theta)) / g
print(f"The horizontal distance is {d:.2f} meters")
