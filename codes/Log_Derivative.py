import sympy as sp

x = sp.symbols('x', positive=True)
s = sp.symbols('s', positive=True)

# y = x^x,  f = (ln y)' = 1 + ln x
y = x**x
f = sp.simplify(sp.diff(sp.log(y), x))
print("f =", f)

# Laplace transform of f
F = sp.laplace_transform(f, x, s, noconds=True)
print("F(s) =", sp.simplify(F))

# L{x f'} = -(sF)'   (since x f -> 0 as x -> 0)
lhs = sp.laplace_transform(x * sp.diff(f, x), x, s, noconds=True)
rhs = -sp.diff(s * F, s)
print("L{x f'}  =", sp.simplify(lhs))
print("-(sF)'   =", sp.simplify(rhs))

# Inverse transform gives x f' = 1
print("x f' =", sp.inverse_laplace_transform(sp.simplify(rhs), s, x))

# Final identity
yp = sp.diff(y, x)
ypp = sp.diff(y, x, 2)
print("y'' - (y')^2/y - y/x =", sp.simplify(ypp - yp**2 / y - y / x))
