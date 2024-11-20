import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 * np.exp(x)

def monte_carlo_integration(num_points=100000, x_max=10):
    # Reduce x_max to a manageable range
    x_min, y_min = 0, f(0)
    y_max = f(x_max)

    # Generate random points
    x = np.random.uniform(x_min, x_max, num_points)
    y = np.random.uniform(y_min, y_max, num_points)

    # Count points under the curve
    points_under_curve = y <= f(x)
    
    # Calculate area
    total_area = (x_max - x_min) * (y_max - y_min)
    area_under_curve = total_area * np.sum(points_under_curve) / num_points

    return area_under_curve, points_under_curve, x, y

# Perform integration
result, points_under_curve, x, y = monte_carlo_integration()

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(x[points_under_curve], y[points_under_curve], c='blue', alpha=0.1, label='Points under curve')
plt.scatter(x[~points_under_curve], y[~points_under_curve], c='red', alpha=0.1, label='Points above curve')

x_curve = np.linspace(0, 10, 1000)
plt.plot(x_curve, f(x_curve), 'g-', label='y = 2e^x')
plt.title(f'Monte Carlo Integration: Area = {result:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print(f"Estimated Area: {result:.2f}")

# Analytical solution for comparison
def analytical_area(x_max=10):
    # Analytical integration of 2e^x from 0 to x_max
    return 2 * (np.exp(x_max) - 1)

print(f"Analytical Area: {analytical_area():.2f}")
