import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the Lotka-Volterra model
def prey_predator(state, t, a, b, c, d):
    x, y = state
    dxdt = a*x - b*x*y
    dydt = c*x*y - d*y
    return [dxdt, dydt]

# Set parameters
a, b, c, d = 1.2, 0.6, 0.2, 0.02
t_span = [0, 300]
initial_state = [0.8, 1.3]

# Create time points
t = np.linspace(t_span[0], t_span[1], 1000)

# Solve ODE
solution = odeint(prey_predator, initial_state, t, args=(a, b, c, d))

# Extract x and y values
x, y = solution.T

# Plot the results
plt.figure(figsize=(12, 6))

# Population over time
plt.subplot(1, 2, 1)
plt.plot(t, x, label='Prey (x)')
plt.plot(t, y, label='Predator (y)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population over Time')
plt.legend()

# Phase plane
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.xlabel('Prey Population (x)')
plt.ylabel('Predator Population (y)')
plt.title('Phase Plane')

plt.tight_layout()
plt.show()

# Print some statistics
print(f"Max prey population: {max(x):.2f}")
print(f"Max predator population: {max(y):.2f}")
print(f"Min prey population: {min(x):.2f}")
print(f"Min predator population: {min(y):.2f}")


# dx = ax-bxy
# dy = cxy-dy

# dx/x = a-by
# dy/y = cx - d

# dx(cx-d)/x = dy(a-by)/y
# (c-d/x)dx = (a/y-b)dy
# cx-dlnx = alny - by

