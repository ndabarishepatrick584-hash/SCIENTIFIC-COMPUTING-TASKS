#Estimate overload risk for a campus online-registration server."""
import numpy as np
import matplotlib.pyplot as plt

capacity = 1000
mean_demand = 850
std_demand = 160  # changed from 120 to test increased uncertainty
number_of_simulations = 100_000
rng = np.random.default_rng(42)

demand = rng.normal(mean_demand, std_demand, number_of_simulations)
overloaded = demand > capacity
probability = overloaded.mean()
running_probability = np.cumsum(overloaded) / np.arange(1, number_of_simulations + 1)

print(f"Server capacity: {capacity} requests")
print(f"Mean simulated demand: {demand.mean():.2f}")
print(f"Simulated overload count: {overloaded.sum()} / {number_of_simulations}")
print(f"Estimated overload probability: {probability:.2%}")

plt.plot(running_probability)
plt.axhline(probability, linestyle="--", label=f"Final estimate = {probability:.2%}")
plt.xlabel("Number of simulations")
plt.ylabel("Running overload probability")
plt.title("Monte Carlo estimate of registration-server overload risk")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("task_20_registration_risk.png", dpi=150)
plt.show()