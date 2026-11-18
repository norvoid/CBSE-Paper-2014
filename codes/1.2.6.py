# 1.2.6  det[[2y, y-z-x, 2y],[2z, 2z, z-x-y],[x-y-z, 2x, 2x]] = (x+y+z)^3
import numpy as np

def D(x, y, z):
    return np.linalg.det(np.array([[2 * y, y - z - x, 2 * y],
                                   [2 * z, 2 * z, z - x - y],
                                   [x - y - z, 2 * x, 2 * x]]))

rng = np.random.default_rng(1)
X = rng.uniform(-3, 3, size=(200, 3))
err = max(abs(D(*v) - v.sum()**3) for v in X)
print("max |det - (x+y+z)^3| over 200 random points =", err)
