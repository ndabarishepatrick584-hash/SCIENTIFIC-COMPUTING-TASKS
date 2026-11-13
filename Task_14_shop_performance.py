#Forecast an online shop's response time under increasing load."""
import numpy as np
import matplotlib.pyplot as plt

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 330], dtype=float)  # changed from 305
coefficients = np.polyfit(users, response_ms, deg=2)
model = np.poly1d(coefficients)
predicted = model(users)
rmse = np.sqrt(np.mean((response_ms - predicted) ** 2))
forecast_users = 400
forecast_ms = model(forecast_users)

print("Quadratic coefficients [a, b, c]:", coefficients)
print(f"Training RMSE: {rmse:.2f} ms")
print(f"Predicted response at {forecast_users} users: {forecast_ms:.2f} ms")
print("The 400-user estimate is extrapolation beyond the measured range.")

x_plot = np.linspace(40, 420, 250)
plt.scatter(users, response_ms, label="Measured response time")
plt.plot(x_plot, model(x_plot), label="Quadratic fit")
plt.scatter([forecast_users], [forecast_ms], marker="x", label="400-user forecast")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Online shop performance model")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("task_14_shop_performance.png", dpi=150)
plt.show()