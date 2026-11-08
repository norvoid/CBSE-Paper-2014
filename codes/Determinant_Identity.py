import sympy as sp

x, y, z = sp.symbols('x y z')
M = sp.Matrix([[2 * y, y - z - x, 2 * y],
               [2 * z, 2 * z, z - x - y],
               [x - y - z, 2 * x, 2 * x]])
d = sp.factor(M.det())
print("det M =", d)
print("det M - (x+y+z)^3 =", sp.simplify(M.det() - (x + y + z)**3))

# Row operation R1 -> R1 + R2 + R3 (left multiplication by an elementary matrix)
E = sp.Matrix([[1, 1, 1], [0, 1, 0], [0, 0, 1]])
print("det E =", E.det())
print("E M first row:", (E * M)[0, :].applyfunc(sp.simplify))
