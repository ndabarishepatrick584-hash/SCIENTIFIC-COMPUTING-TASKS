#Rank connected devices in a small office network."""
import numpy as np

nodes = ["Router", "Laptop A", "Laptop B", "Printer"]
# Undirected links; connection between Laptop A and Printer is removed.
adjacency = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(adjacency)
index = np.argmax(eigenvalues.real)
dominant_eigenvalue = eigenvalues[index].real
scores = np.abs(eigenvectors[:, index].real)
scores = scores / scores.sum()

print("Nodes:", nodes)
print(f"Dominant eigenvalue: {dominant_eigenvalue:.6f}")
print("Relative eigenvector scores:")
for node, score in sorted(zip(nodes, scores), key=lambda item: item[1], reverse=True):
    print(f"  {node}: {score:.4f}")
print("Scores represent structural influence, not traffic or security.")