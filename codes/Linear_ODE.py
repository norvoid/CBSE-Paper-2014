import sympy as sp

x = sp.symbols('x')
C1 = sp.symbols('C1')
y = sp.Function('y')

ode = sp.Eq((x**2 - 1) * y(x).diff(x) + 2 * x * y(x), 2 / (x**2 - 1))
sol = sp.dsolve(ode, y(x))
print(sol)

# Check the claimed solution y = [ln|(x-1)/(x+1)| + C] / (x^2 - 1) for x > 1
yc = (sp.log((x - 1) / (x + 1)) + C1) / (x**2 - 1)
res = (x**2 - 1) * sp.diff(yc, x) + 2 * x * yc - 2 / (x**2 - 1)
print("Residual:", sp.simplify(res))
