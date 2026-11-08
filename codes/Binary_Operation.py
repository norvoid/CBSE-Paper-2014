import sympy as sp

# Binary operation a*b = ab/5 on non-zero reals
def star(a, b):
    return a * b / 5

x = sp.symbols('x', real=True, nonzero=True)
a, b, c = sp.symbols('a b c', real=True, nonzero=True)

# Solve 2*(x*5) = 10
sol = sp.solve(sp.Eq(star(2, star(x, 5)), 10), x)
print("x =", sol)

# 5 is the identity and * is associative
print("a*5 - a             =", sp.simplify(star(a, 5) - a))
print("(a*b)*c - a*(b*c)   =", sp.simplify(star(star(a, b), c) - star(a, star(b, c))))

# Scaling phi(a) = a/5 turns * into ordinary multiplication
phi = lambda t: t / 5
print("phi(a*b) - phi(a)phi(b) =", sp.simplify(phi(star(a, b)) - phi(a) * phi(b)))
