import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return t + 2 * y

def euler_method(f, y0, t0, tn, h):
    n = int((tn - t0) / h)
    t = np.linspace(t0, tn, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    for i in range(1, n+1):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1])
    
    return t, y

# Initial conditions and parameters
y0 = 1
t0 = 1
tn = 2
h = 0.1

# Simulate using Euler's method
t, y = euler_method(f, y0, t0, tn, h)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, y, 'b-', label='Numerical Solution')
plt.title("Euler's Method: dy/dt = t + 2y, y(1) = 1")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Print the results
print("t\t\ty")
for ti, yi in zip(t, y):
    print(f"{ti:.2f}\t\t{yi:.6f}")