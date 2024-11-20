import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

A = 0.7 # birth rate
B = 0.3 # death rate
H = 300 # harvesting rate


def model(t, state):
    f = state
    dfdt = A * f - B * f - 300
    return [dfdt]

time_span = (0, 20)
initial_condition = [800]
sol = solve_ivp(model, time_span, initial_condition, t_eval=np.linspace(0, 20, 20))

t = sol.t
y = sol.y[0]

plt.xlabel("Days")
plt.ylabel("Fish Population")
plt.title("Growth of fish population over time")
plt.grid(True)
plt.plot(t, y)
plt.show()