# 1.2.13  3x + 2y + z = 1000, 4x + y + 3z = 1500, x + y + z = 600 by Gaussian elimination
import numpy as np

def gauss_solve(A, b):
    """Solve Ax = b by Gaussian elimination with partial pivoting and back substitution."""
    M = np.hstack([A.astype(float), b.reshape(-1, 1).astype(float)])
    n = A.shape[0]
    for k in range(n):
        p = k + np.argmax(np.abs(M[k:, k]))
        M[[k, p]] = M[[p, k]]
        for i in range(k + 1, n):
            M[i] -= M[i, k] / M[k, k] * M[k]
    print("Echelon form:\n", np.round(M, 4))
    sol = np.zeros(n)
    for k in range(n - 1, -1, -1):
        sol[k] = (M[k, -1] - M[k, k + 1:n] @ sol[k + 1:]) / M[k, k]
    return sol

A = np.array([[3, 2, 1], [4, 1, 3], [1, 1, 1]])
b = np.array([1000, 1500, 600])
X = gauss_solve(A, b)
print("Discipline, Politeness, Punctuality =", X, ", check A x =", A @ X)
