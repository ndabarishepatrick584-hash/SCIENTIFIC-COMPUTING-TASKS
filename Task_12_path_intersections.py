#Find intersections of a circular boundary and a curved path."""
import numpy as np
from scipy.optimize import root

# Circle: x² + y² = 4; parabola: y = x² - 1
def equations(z):
    x, y = z
    return np.array([x**2 + y**2 - 4, y - (x**2 - 1)])

# One initial guess changed to [2, 2].
for guess in ([2.0, 2.0], [-1.0, 1.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Solver converged:", solution.success)
    print("Intersection estimate [x, y]:", np.round(solution.x, 8))
    print("Residuals:", np.round(equations(solution.x), 10))
    print()