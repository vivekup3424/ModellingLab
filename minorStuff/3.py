import numpy as np
import matplotlib.pyplot as plt

# Given constants
cin = 3
V = 28
F = 4*12
C0 = 10
tspan = [0, 4]
N = 100

# Time vector
t = np.linspace(tspan[0], tspan[1], N)

# Differential equation function
def lake_pollution(t, c):
    return (F * cin / V) - (F * c / V)

# Initialize concentration array
c = np.zeros(N)
c[0] = C0  # Initial condition

# Time step
dt = (tspan[1] - tspan[0]) / (N - 1)

# Euler's method to solve the differential equation
for i in range(1, N):
    c[i] = c[i-1] + lake_pollution(t[i-1], c[i-1]) * dt

# Plotting the results
plt.plot(t, c, label="Concentration of pollutants")
plt.xlabel("Time (t)")
plt.ylabel("Concentration (c)")
plt.title("Simulation of Lake Pollution")
plt.legend()
plt.grid(True)
plt.show()



