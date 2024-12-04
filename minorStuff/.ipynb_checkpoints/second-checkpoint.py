import numpy as np
import matplotlib.pyplot as plt 


def f(t, y):
    return y**2 + t
def euler_method(f, t0, y0, tn, h):
    n = int((tn - t0)/h)

    t_values = np.linspace(t0, tn, n + 1)
    y_values = np.zeros(n + 1)

    y_values[0] = 1
    t_values[0] = 0
    for i in range(n):
        y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
        print(t_values[i])
    return t_values, y_values

t0 = 0   # Initial time
y0 = 1   # Initial value of y
t_end = .2  # End time
h = 0.1  # Step size

# Solve the equation
t_values, y_values = euler_method(f, t0, y0, t_end, h)
plt.plot(t_values, y_values, label='Euler Approximation')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Euler Method Approximation')
plt.legend()
plt.grid(True)
plt.show()