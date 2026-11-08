import numpy as np
import sympy as sp

x = sp.symbols('x', real=True)
L = sp.Matrix([[2 * x, 5], [8, x]]).det()
R = sp.Matrix([[6, -2], [7, 3]]).det()
print("det L =", sp.expand(L), ", det R =", R)
print("x =", sp.solve(sp.Eq(L, R), x))

# Numerical check
for x0 in (6.0, -6.0):
    M = np.array([[2 * x0, 5], [8, x0]])
    print(x0, np.linalg.det(M))
