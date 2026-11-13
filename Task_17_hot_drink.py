#Predict cooling of a hot drink using Euler's method.
import numpy as np
import matplotlib.pyplot as plt

ambient_c = 25.0
initial_c = 90.0
cooling_k = 0.12  # per minute
step_min = 0.5  # changed from 1.0 minute
duration_min = 30.0

time_min = np.arange(0, duration_min + step_min, step_min)
euler_temp = np.zeros_like(time_min)
euler_temp[0] = initial_c

for i in range(1, len(time_min)):
    euler_temp[i] = euler_temp[i-1] + step_min * (
        -cooling_k * (euler_temp[i-1] - ambient_c)
    )

exact_temp = ambient_c + (initial_c - ambient_c) * np.exp(-cooling_k * time_min)
error = np.abs(euler_temp - exact_temp)

print(f"Euler temperature after {duration_min:.0f} min: {euler_temp[-1]:.3f} °C")
print(f"Exact temperature after {duration_min:.0f} min: {exact_temp[-1]:.3f} °C")
print(f"Maximum absolute error: {np.max(error):.4f} °C")

plt.plot(time_min, euler_temp, "o-", markevery=5, label="Euler approximation")
plt.plot(time_min, exact_temp, label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Drink temperature (°C)")
plt.title("Cooling of a hot drink")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("task_17_hot_drink.png", dpi=150)
plt.show()