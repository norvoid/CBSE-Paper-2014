import numpy as np

# Relation (a,b) R (c,d) iff a + d = b + c on A x A, A = {1,...,9}
A = range(1, 10)
pts = [(a, b) for a in A for b in A]
n = len(pts)

R = np.zeros((n, n), dtype=bool)
for i, (a, b) in enumerate(pts):
    for j, (c, d) in enumerate(pts):
        R[i, j] = (a + d == b + c)

reflexive = np.all(np.diag(R))
symmetric = np.array_equal(R, R.T)
# Transitive: R o R is contained in R
RR = (R.astype(int) @ R.astype(int)) > 0
transitive = np.all(R[RR])
print("Reflexive :", reflexive)
print("Symmetric :", symmetric)
print("Transitive:", transitive)

# Equivalence class of (2,5)
i0 = pts.index((2, 5))
print("[(2,5)] =", [pts[j] for j in range(n) if R[i0, j]])
