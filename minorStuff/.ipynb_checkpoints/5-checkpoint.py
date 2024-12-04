import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def predator_prey_model(state, t, R, K, B, C, D):
    X, Y = state
    dXdt = R * X * (1 - X / K) - B * X * Y
    dYdt = C * X * Y - D * Y
    return [dXdt, dYdt]

# Set parameters
R = 1.0  # Growth rate of prey
K = 100.0  # Carrying capacity of prey
B = 0.02  # Predation rate
C = 0.01  # Reproduction rate of predators per prey eaten
D = 0.1  # Death rate of predators

# Initial conditions
X0 = 50  # Initial prey population
Y0 = 20  # Initial predator population
initial_state = [X0, Y0]

# Time span
tspan = np.linspace(0, 1000, 10000)

# Solve ODE
solution = odeint(predator_prey_model, initial_state, tspan, args=(R, K, B, C, D))

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(tspan, solution[:, 0], 'b', label='Prey (X)')
plt.plot(tspan, solution[:, 1], 'r', label='Predator (Y)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Predator-Prey Model Simulation')
plt.legend()
plt.grid(True)
plt.show()

# Print final populations
print(f"Final prey population: {solution[-1, 0]:.2f}")
print(f"Final predator population: {solution[-1, 1]:.2f}")