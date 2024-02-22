# %% markdown
# # Physics with Python
# We will use Python to solve physics problems. Don't be afraid of the code, it is very simple and easy to understand.
# secondly we can use GPT to explain and modify the code.

# %% codecell
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


# %% codecell
# Plot sin(x) and cos(x) from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label="sin(x)", color="r")
plt.plot(x, y2, label="cos(x)", color="b")
plt.legend()
plt.show()

# %% codecell
# plot circle
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y)
plt.axis("equal")
plt.show()


# %% codecell
# solve a y'(x)=-y(x) with y(0)=1 using Euler's method
def f(x, y):
    return -y


x = 0
y = 1
h = 0.001
X = [x]
Y = [y]
for i in range(10000):
    y = y + h * f(x, y)
    x = x + h
    X.append(x)
    Y.append(y)
plt.plot(X, Y)
plt.show()

# %% codecell
# solve a y''(x)=-y(x) with y(0)=0 and y'(0)=1 using Euler's method
# What is wrong with this numerical solution?
