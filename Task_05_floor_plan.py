# Scale and rotate points on a simple floor-plan drawing."""
import numpy as np

points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])
angle_degrees = 90  # change to 45 to compare the transformed floor plan
angle = np.deg2rad(angle_degrees)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])
scale = np.array([[2.0, 0.0], [0.0, 1.5]])
transformation = rotation @ scale
transformed_points = points @ transformation.T

print("Original floor-plan points:\n", points)
print(f"Rotation angle: {angle_degrees} degrees")
print("Transformed points:\n", np.round(transformed_points, 4))
print(f"Determinant: {np.linalg.det(transformation):.4f}")
print("The determinant magnitude is the area-scaling factor.")