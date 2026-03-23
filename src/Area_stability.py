import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
A = 1.0  # Amplitude
omega = 2 * np.pi  # Frequency

def static_ode(X, t):
    x, y = X
    dxdt = A * np.sin(omega * t) - x
    dydt = -y
    return [dxdt, dydt]

# GCD computation function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# First-return map analysis
def first_return_map(x_values):
    # Assuming x_values contains the x-coordinate of the trajectory
    return x_values[1:], x_values[:-1]  # Dummy example of a map

# Simulation parameters
T = 10.0  # total time
n_points = 1000
t = np.linspace(0, T, n_points)
initial_conditions = [0, 1]

# Solve ODE
solution = odeint(static_ode, initial_conditions, t)

# Area stability analysis
x_values = solution[:, 0]
return_map_x, return_map_y = first_return_map(x_values)

# Scatter plot generation
plt.figure(figsize=(8, 6))
plt.scatter(return_map_x, return_map_y, s=5, color='r')
plt.title('First-Return Map')
plt.xlabel('X (n)')
plt.ylabel('X (n+1)')
plt.grid(True)
plt.axis('equal')
plt.savefig('first_return_map.png')
plt.show()