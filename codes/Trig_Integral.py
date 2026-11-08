import sympy as sp

x = sp.symbols('x')
integrand = (sp.sin(x)**6 + sp.cos(x)**6) / (sp.sin(x)**2 * sp.cos(x)**2)
F = sp.tan(x) - sp.cot(x) - 3 * x

# F'(x) must equal the integrand
print("F' - f =", sp.simplify(sp.diff(F, x) - integrand))

# Numerical check at random points
import numpy as np
f = sp.lambdify(x, integrand, 'numpy')
dF = sp.lambdify(x, sp.diff(F, x), 'numpy')
pts = np.array([0.3, 0.7, 1.1, 1.4])
print(f(pts) - dF(pts))
