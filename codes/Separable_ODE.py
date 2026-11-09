import numpy as np
import sympy as sp

x = sp.symbols('x', positive=True)
s = sp.symbols('s', positive=True)

# z = sqrt(1-y^2):  dz/dx = x e^x,  z(0) = 0
G = sp.laplace_transform(x * sp.exp(x), x, s, noconds=True)
print("L{x e^x} =", sp.simplify(G))

Z = G / s                                  # sZ - z(0) = G, z(0) = 0
print("Z(s) =", sp.simplify(Z))
print("Partial fractions:", sp.apart(sp.simplify(Z), s))

z = sp.simplify(sp.inverse_laplace_transform(sp.apart(sp.simplify(Z), s), s, x))
print("z(x) =", z)

# Check against the solution (x-1)e^x + 1
print("z - ((x-1)e^x + 1) =", sp.simplify(z - ((x - 1) * sp.exp(x) + 1)))

# Check the original ODE numerically:  e^x sqrt(1-y^2) + (y/x) dy/dx = 0
y = sp.sqrt(1 - ((x - 1) * sp.exp(x) + 1)**2)
res = sp.exp(x) * sp.sqrt(1 - y**2) + (y / x) * sp.diff(y, x)
r = sp.lambdify(x, res, 'numpy')
print("Residual at x = 0.2, 0.4, 0.6:", r(np.array([0.2, 0.4, 0.6])))
