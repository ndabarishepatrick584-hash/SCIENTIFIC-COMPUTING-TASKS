# Check a sensor calibration calculation and numerical error."""
import numpy as np

reference_value = np.sqrt(2)
measured_value = 1.4142  # change this value to test a different measurement

absolute_error = abs(reference_value - measured_value)
relative_error = absolute_error / abs(reference_value)

calculated = 0.1 + 0.2
expected = 0.3

print("0.1 + 0.2 =", calculated)
print("Exact equality:", calculated == expected)
print("Equal within tolerance:", np.isclose(calculated, expected))
print(f"Reference sqrt(2): {reference_value:.10f}")
print(f"Measured/approximate value: {measured_value:.10f}")
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.6%}")