#Estimate two machine types from CPU and memory totals."""
import numpy as np

# Type A uses 4 CPU units and 8 GB memory.
# Type B uses 2 CPU units and 12 GB memory.
# Fractional values are mathematical estimates; real machines are whole units.
A = np.array([[4.0, 2.0], [8.0, 12.0]])
cpu_total = 22.0  # changed from 20 to demonstrate parameter sensitivity
memory_total = 72.0
b = np.array([cpu_total, memory_total])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Estimated Type A quantity: {solution[0]:.3f}")
print(f"Estimated Type B quantity: {solution[1]:.3f}")
print("Reconstructed totals [CPU, memory]:", A @ solution)
print("Residual:", residual)
print("Note: integer machine counts require an integer-optimization model.")