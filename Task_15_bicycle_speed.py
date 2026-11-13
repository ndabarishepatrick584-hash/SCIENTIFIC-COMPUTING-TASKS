# Estimate bicycle speed from GPS position samples."""
import numpy as np
import matplotlib.pyplot as plt

time_s = np.arange(0, 7, dtype=float)
position_m = np.array([0.0, 4.8, 10.2, 17.1, 22.7, 30.0, 38.0])  # t=3 position changed
speed_ms = np.empty_like(position_m)
speed_ms[0] = (position_m[1] - position_m[0]) / (time_s[1] - time_s[0])
speed_ms[-1] = (position_m[-1] - position_m[-2]) / (time_s[-1] - time_s[-2])
speed_ms[1:-1] = (position_m[2:] - position_m[:-2]) / (time_s[2:] - time_s[:-2])

print("Time (s):", time_s)
print("Estimated speed (m/s):", np.round(speed_ms, 3))

plt.plot(time_s, speed_ms, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Bicycle speed from GPS positions")
plt.grid(True)
plt.tight_layout()
plt.savefig("task_15_bicycle_speed.png", dpi=150)
plt.show()