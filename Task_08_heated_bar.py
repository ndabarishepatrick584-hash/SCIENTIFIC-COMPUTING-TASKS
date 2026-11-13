# Estimate steady-state temperatures along a heated bar."""
import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [2, -1, 0, 0, 0],
    [-1, 2, -1, 0, 0],
    [0, -1, 2, -1, 0],
    [0, 0, -1, 2, -1],
    [0, 0, 0, -1, 2]
], dtype=float)
b = np.array([100.0, 0.0, 0.0, 0.0, 20.0])
tolerance = 1e-4  # change to 1e-8 for a tighter stopping condition
max_iterations = 500

def jacobi(A, b, tol, max_iter):
    x = np.zeros_like(b)
    D = np.diag(A)
    R = A - np.diagflat(D)
    errors = []
    for iteration in range(1, max_iter + 1):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        x = x_new
        if error < tol:
            return x, errors
    return x, errors

def gauss_seidel(A, b, tol, max_iter):
    x = np.zeros_like(b)
    errors = []
    for iteration in range(1, max_iter + 1):
        old = x.copy()
        for i in range(len(b)):
            left = A[i, :i] @ x[:i]
            right = A[i, i+1:] @ old[i+1:]
            x[i] = (b[i] - left - right) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

x_j, err_j = jacobi(A, b, tolerance, max_iterations)
x_g, err_g = gauss_seidel(A, b, tolerance, max_iterations)
x_direct = np.linalg.solve(A, b)

print("Jacobi temperatures (°C):", np.round(x_j, 4))
print("Gauss-Seidel temperatures (°C):", np.round(x_g, 4))
print("Direct solution (°C):", np.round(x_direct, 4))
print(f"Jacobi iterations: {len(err_j)}; Gauss-Seidel iterations: {len(err_g)}")

plt.semilogy(range(1, len(err_j)+1), err_j, label="Jacobi")
plt.semilogy(range(1, len(err_g)+1), err_g, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Change between iterations (∞-norm)")
plt.title("Heated-bar convergence")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("task_08_heated_bar_convergence.png", dpi=150)
plt.show()