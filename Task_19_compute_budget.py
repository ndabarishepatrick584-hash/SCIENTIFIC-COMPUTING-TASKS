#Choose a least-cost compute allocation for a student web application.
import numpy as np
from scipy.optimize import minimize

cost = np.array([12.0, 18.0])       # cost per Type A and Type B unit
capacity = np.array([100.0, 170.0]) # capacity per unit
required_capacity = 1200.0          # changed from 1000

def objective(x):
    return cost @ x

# Constraint must be non-negative: capacity @ x - requirement >= 0.
constraint = {"type": "ineq",
              "fun": lambda x: capacity @ x - required_capacity}
result = minimize(objective, x0=np.array([5.0, 5.0]),
                  bounds=[(0, None), (0, None)],
                  constraints=[constraint], method="SLSQP")

print("Continuous optimization successful:", result.success)
print("Continuous allocation [Type A, Type B]:", np.round(result.x, 4))
print(f"Continuous cost: {objective(result.x):.2f}")
print(f"Continuous capacity: {capacity @ result.x:.2f}")

# Whole-unit search for a practical feasible candidate.
best = None
for a in range(0, int(required_capacity / capacity[0]) + 2):
    for b in range(0, int(required_capacity / capacity[1]) + 2):
        total_capacity = capacity @ np.array([a, b])
        total_cost = cost @ np.array([a, b])
        if total_capacity >= required_capacity:
            candidate = (total_cost, a, b, total_capacity)
            if best is None or candidate[0] < best[0]:
                best = candidate

print(f"Best whole-unit allocation: Type A={best[1]}, Type B={best[2]}")
print(f"Whole-unit cost: {best[0]:.2f}")
print(f"Whole-unit capacity: {best[3]:.2f}")