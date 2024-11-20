import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def model(t, P, r):
    dPdt = r*P
    return dPdt

P0 = 1e6
r = 0.5
t_span = (0,500)

sol = solve_ivp(lambda t, P: model(t, P, r), t_span, [P0], t_eval=np.linspace(0,500,501))

t = sol.t
P = sol.y[0]

plt.figure(figsize=(8,6))
plt.plot(t,P)
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.title('Population Growth Simulation')
plt.grid()
plt.show()


