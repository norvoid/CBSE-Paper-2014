# 1.2.11  Intersection of x = A1 + lam m1 and x = A2 + mu m2 by Gaussian elimination
import numpy as np
import matplotlib.pyplot as plt

def row_echelon(M):
    M = M.astype(float).copy()
    m, n = M.shape
    r = 0
    for c in range(n):
        if r == m:
            break
        p = r + np.argmax(np.abs(M[r:, c]))
        if abs(M[p, c]) < 1e-12:
            continue
        M[[r, p]] = M[[p, r]]
        for i in range(r + 1, m):
            M[i] -= M[i, c] / M[r, c] * M[r]
        r += 1
    return M

A1 = np.array([-1.0, -3.0, -5.0])
m1 = np.array([3.0, 5.0, 7.0])
A2 = np.array([2.0, 4.0, 6.0])
m2 = np.array([1.0, 3.0, 5.0])

M = np.column_stack([m1, -m2])
Mb = np.column_stack([M, A2 - A1])
E = row_echelon(Mb)
print("Echelon form of [M | A2 - A1]:\n", np.round(E, 6))
rank_M = np.sum(np.any(np.abs(E[:, :2]) > 1e-9, axis=1))
rank_Mb = np.sum(np.any(np.abs(E) > 1e-9, axis=1))
print("rank(M) =", rank_M, ", rank([M | b]) =", rank_Mb)

mu = E[1, 2] / E[1, 1]                       # back substitution
lam = (E[0, 2] - E[0, 1] * mu) / E[0, 0]
P = A1 + lam * m1
print("lambda =", lam, ", mu =", mu)
print("Point of intersection:", P, ", on line 2:", A2 + mu * m2)

t = np.linspace(-1.5, 2.0, 50)
L1 = A1[:, None] + m1[:, None] * t
L2 = A2[:, None] + m2[:, None] * t
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
ax.plot(*L1, 'b-', label='Line 1')
ax.plot(*L2, 'g-', label='Line 2')
ax.plot(*P, 'ro', markersize=8, label='Intersection')
ax.text(P[0], P[1], P[2] + 0.8, r'$\left(\frac{1}{2}, -\frac{1}{2}, -\frac{3}{2}\right)$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('figs/1.2.11.png')
