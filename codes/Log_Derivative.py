import sympy as sp

x = sp.symbols('x', positive=True)
y = x**x
yp = sp.diff(y, x)
ypp = sp.diff(y, x, 2)
print("y'  =", sp.simplify(yp))
print("y'' - (y')^2/y - y/x =", sp.simplify(ypp - yp**2 / y - y / x))

# (y'/y)' = y''/y - (y'/y)^2 = (ln y)''
print("(ln y)''  =", sp.simplify(sp.diff(sp.log(y), x, 2)))
