import numpy as np
import sympy as sp

x, t, s, w0 = sp.symbols('x t s w0', real=True)

# For 0 <= x < 1, put x = tanh t and w = (x^2-1) y.  Then dw/dt = -2.
# Laplace transform:  s W - w(0) = -2/s
W = (w0 - 2 / s) / s
print("W(s) =", sp.expand(W))
w_t = sp.inverse_laplace_transform(sp.expand(W), s, t)
print("w(t) =", sp.simplify(w_t))

# Back to x:  t = atanh(x)
w_x = (w0 - 2 * sp.atanh(x))
y = w_x / (x**2 - 1)

# Compare with ln((1-x)/(1+x)) :  -2 atanh(x) = ln((1-x)/(1+x))
xs = np.array([0.1, 0.4, 0.7])
print("-2 atanh(x) - ln((1-x)/(1+x)) =", -2 * np.arctanh(xs) - np.log((1 - xs) / (1 + xs)))

# Check the original ODE numerically with w0 = C = 3
yy = y.subs(w0, 3)
res = (x**2 - 1) * sp.diff(yy, x) + 2 * x * yy - 2 / (x**2 - 1)
r = sp.lambdify(x, res, 'numpy')
print("Residual at x = 0.1, 0.4, 0.7:", r(np.array([0.1, 0.4, 0.7])))
