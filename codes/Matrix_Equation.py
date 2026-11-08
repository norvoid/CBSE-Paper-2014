import numpy as np
import sympy as sp

x, y = sp.symbols('x y')
A = sp.Matrix([[3, 4], [5, x]])
B = sp.Matrix([[1, y], [0, 1]])
C = sp.Matrix([[7, 0], [10, 5]])

# Entry-wise equations of 2A + B - C = 0 (non-trivial ones)
eqs = [e for e in (2 * A + B - C) if e != 0]
print("Equations:", eqs)

sol = sp.solve(eqs, [x, y])
print("Solution:", sol)
print("x - y =", sol[x] - sol[y])

# Numerical check with the solved values
A_n = np.array([[3, 4], [5, float(sol[x])]])
B_n = np.array([[1, float(sol[y])], [0, 1]])
print(2 * A_n + B_n)
