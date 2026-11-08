import numpy as np

a = np.array([1.0, 3.0, 7.0]).reshape(-1, 1)
b = np.array([2.0, -3.0, 6.0]).reshape(-1, 1)

# Scalar projection of a on b
proj = (a.T @ b).item() / np.linalg.norm(b)
print("a^T b      =", (a.T @ b).item())
print("||b||      =", np.linalg.norm(b))
print("Projection =", proj)
