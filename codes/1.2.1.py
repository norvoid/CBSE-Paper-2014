# 1.2.1  [x 1][[1,0],[-2,0]] = O
import numpy as np

B = np.array([[1, 0], [-2, 0]])
x = 2
print("[x 1] B =", np.array([x, 1]) @ B)
