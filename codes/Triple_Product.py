import numpy as np

rng = np.random.default_rng(1)
a = rng.standard_normal((3, 1))
b = rng.standard_normal((3, 1))
c = rng.standard_normal((3, 1))

M = np.block([a, b, c])
N = np.block([a + b, b + c, c + a])

# N = M T, with the columns of T giving the coefficients
T = np.array([[1, 0, 1],
              [1, 1, 0],
              [0, 1, 1]])
print("N - M T =\n", N - M @ T)
print("det T   =", np.linalg.det(T))
print("[a+b,b+c,c+a] =", np.linalg.det(N))
print("2[a,b,c]      =", 2 * np.linalg.det(M))
