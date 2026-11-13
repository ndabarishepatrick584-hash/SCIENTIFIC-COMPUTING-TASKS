#Simulate capacitor charging in a backup circuit with SciPy."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

supply_v = 5.0
resistance_ohm = 1000.0
capacitance_f = 0.002  # changed from 0.001 F
initial_voltage_v = 0.0
start_s, end_s = 0.0, 5.0

time_points = np.linspace(start_s, end_s, 300)
time_constant = resistance_ohm * capacitance_f

def circuit_ode(t, y):
    voltage = y[0]
    return [(supply_v - voltage) / time_constant]

solution = solve_ivp(
    circuit_ode, (start_s, end_s), [initial_voltage_v],
    t_eval=time_points, rtol=1e-9, atol=1e-11
)
numerical_v = solution.y[0]
exact_v = supply_v + (initial_voltage_v - supply_v) * np.exp(-time_points / time_constant)

print(f"Time constant RC: {time_constant:.3f} s")
print(f"Numerical voltage at 5 s: {numerical_v[-1]:.4f} V")
print(f"Exact voltage at 5 s: {exact_v[-1]:.4f} V")
print(f"Maximum absolute error: {np.max(np.abs(numerical_v-exact_v)):.3e} V")

plt.plot(time_points, numerical_v, label="SciPy solve_ivp")
plt.plot(time_points, exact_v, "--", label="Exact solution")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("Backup-circuit capacitor charging")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("task_18_backup_circuit.png", dpi=150)
plt.show()