# 1.2.10a  [a+b, b+c, c+a] = 2[a, b, c]  (triple product as a determinant)
import numpy as np

def triple(a, b, c):
    return np.linalg.det(np.column_stack([a, b, c]))

rng = np.random.default_rng(0)
err = 0.0
for _ in range(1000):
    a, b, c = rng.normal(size=(3, 3))
    err = max(err, abs(triple(a + b, b + c, c + a) - 2 * triple(a, b, c)))
print("max error over 1000 random triples =", err)
