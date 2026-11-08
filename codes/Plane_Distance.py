import numpy as np

A = np.array([2.0, 5.0, -3.0]).reshape(-1, 1)
B = np.array([-2.0, -3.0, 5.0]).reshape(-1, 1)
C = np.array([5.0, 3.0, -3.0]).reshape(-1, 1)
P = np.array([7.0, 2.0, 4.0]).reshape(-1, 1)

# Normal vector n satisfies  n^T (B-A) = 0, n^T (C-A) = 0  ->  null space
M = np.block([B - A, C - A]).T
U, S, Vt = np.linalg.svd(M)
n = Vt[-1].reshape(-1, 1)
n = n / n[0, 0] * 2                      # scale so that n = (2, 3, 4)^T
c = (n.T @ A).item()
print("n =", n.flatten(), ", c =", c)
print("n^T B =", (n.T @ B).item(), ", n^T C =", (n.T @ C).item())

# Distance of P from the plane
d = abs((n.T @ P).item() - c) / np.linalg.norm(n)
print("Distance =", d, ", sqrt(29) =", np.sqrt(29))
