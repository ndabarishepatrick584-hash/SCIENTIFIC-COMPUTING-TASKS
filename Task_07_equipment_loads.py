# Repeatedly estimate equipment loads using LU decomposition."""
import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])
# First vector changed from [15, 10, 10] to [16, 10, 10].
measurement_sets = [
    np.array([16.0, 10.0, 10.0]),
    np.array([16.0, 11.0, 9.0]),
    np.array([14.0, 12.0, 11.0])
]

lu, piv = lu_factor(A)  # factor the unchanged matrix only once
for index, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x
    print(f"Measurement set {index}:")
    print("Estimated equipment loads:", np.round(x, 6))
    print(f"Residual norm: {np.linalg.norm(residual):.3e}\n")