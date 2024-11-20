import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def sir_model(y, t, B, C):
    S, I, R = y
    dSdt = -B*S*I
    dIdt = B*S*I - C*I
    dRdt = C*I
    return dSdt, dIdt, dRdt


B = .3
C = .1
N = 1000
I0 = 1
S0 = 999
R0 = 0
intial_con = (S0, I0, R0)


t = np.linspace(0, 160, 160)

solution = odeint(sir_model, intial_con, t, args=(B,C))
S, I, R = solution.T


plt.figure(figsize=(10, 6))
plt.plot(t, S, label="Susceptible")
plt.plot(t, I, label="Infected")
plt.plot(t, R, label="Recovered")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.title("SIR")
plt.grid(True)
plt.show()