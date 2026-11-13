#Estimate daily electrical energy from smart-meter power readings."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

time_hours = np.arange(0, 14, 2, dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 2.0, 1.6, 1.2, 0.9])  # 6-hour reading changed to 2.0 kW

trapezoid_energy = np.trapezoid(power_kw, time_hours)
simpson_energy = simpson(power_kw, x=time_hours)

print(f"Trapezoidal energy estimate: {trapezoid_energy:.3f} kWh")
print(f"Simpson energy estimate: {simpson_energy:.3f} kWh")
print(f"Difference: {abs(trapezoid_energy - simpson_energy):.3f} kWh")

plt.plot(time_hours, power_kw, marker="o")
plt.fill_between(time_hours, power_kw, alpha=0.2)
plt.xlabel("Time (hours)")
plt.ylabel("Power (kW)")
plt.title("Smart-meter power readings")
plt.grid(True)
plt.tight_layout()
plt.savefig("task_16_meter_power.png", dpi=150)
plt.show()