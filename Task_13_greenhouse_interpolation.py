# Estimate greenhouse temperature every ten minutes."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# Hours after 08:00; measurements are hourly.
hours = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
temps_c = np.array([19.0, 21.0, 22.5, 26.0, 25.0, 23.0, 21.5])  # 11:00 changed to 26°C

linear = interp1d(hours, temps_c, kind="linear")
spline = CubicSpline(hours, temps_c)
target_hours = np.arange(0, 6.0001, 1/6)  # every ten minutes

print("Estimates around 10:30:")
print(f"Linear at 10:30: {float(linear(2.5)):.2f} °C")
print(f"Cubic spline at 10:30: {float(spline(2.5)):.2f} °C")
print("First six ten-minute estimates (linear):", np.round(linear(target_hours[:6]), 2))

plt.scatter(hours, temps_c, label="Measured hourly readings")
plt.plot(target_hours, linear(target_hours), label="Linear interpolation")
plt.plot(target_hours, spline(target_hours), label="Cubic spline")
plt.xlabel("Hours after 08:00")
plt.ylabel("Temperature (°C)")
plt.title("Greenhouse temperature interpolation")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("task_13_greenhouse_interpolation.png", dpi=150)
plt.show()