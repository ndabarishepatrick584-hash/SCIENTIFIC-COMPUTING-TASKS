#Estimate a thermostat's equilibrium temperature."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

def heat_balance(T):
    return T - 25.0 - 10.0 * np.exp(-T / 20.0)

bracket_root = root_scalar(heat_balance, bracket=[20.0, 40.0],
                           method="bisect", xtol=1e-10)
initial_guess = 35.0  # changed from 30°C
# Fixed-point form: T = 25 + 10 exp(-T/20)
T = initial_guess
tolerance = 1e-10
for iteration in range(1, 10001):
    new_T = 25.0 + 10.0 * np.exp(-T / 20.0)
    if abs(new_T - T) < tolerance:
        T = new_T
        break
    T = new_T

print(f"Bisection equilibrium: {bracket_root.root:.8f} °C")
print(f"Fixed-point equilibrium: {T:.8f} °C")
print(f"Residual f(T): {heat_balance(T):.3e}")
print(f"Fixed-point iterations: {iteration}")

temperatures = np.linspace(15, 40, 300)
plt.plot(temperatures, heat_balance(temperatures), label="f(T)")
plt.axhline(0, linestyle="--", label="Zero balance")
plt.axvline(bracket_root.root, linestyle=":", label="Equilibrium")
plt.xlabel("Temperature T (°C)")
plt.ylabel("Heat-balance function f(T)")
plt.title("Thermostat equilibrium")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("task_10_thermostat_root.png", dpi=150)
plt.show()