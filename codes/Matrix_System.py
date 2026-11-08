import numpy as np

# Rows: school P, school Q, one prize per value
A = np.array([[3, 2, 1],
              [4, 1, 3],
              [1, 1, 1]], dtype=float)
b = np.array([1000, 1500, 600], dtype=float).reshape(-1, 1)

print("det A =", np.linalg.det(A))
print("A^{-1} * det A (adjoint) =\n", np.round(np.linalg.inv(A) * np.linalg.det(A), 6))
x = np.linalg.solve(A, b)
print("[x, y, z] =", x.flatten())

# Cramer's rule
for i in range(3):
    Ai = A.copy()
    Ai[:, i] = b.flatten()
    print("Cramer", i + 1, "=", np.linalg.det(Ai) / np.linalg.det(A))
