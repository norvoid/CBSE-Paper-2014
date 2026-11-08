import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Critical points of f(x) = 3x^4 - 4x^3 - 12x^2 + 5
x = sp.symbols('x', real=True)
f = 3 * x**4 - 4 * x**3 - 12 * x**2 + 5
df = sp.diff(f, x)
print("f'(x) =", sp.factor(df))
crit = sp.solve(df, x)
print("Critical points:", crit)

fn = sp.lambdify(x, f, 'numpy')
dfn = sp.lambdify(x, df, 'numpy')

# Sign of f' on each interval
edges = [-3] + sorted(crit) + [4]
for lo, hi in zip(edges[:-1], edges[1:]):
    m = 0.5 * (lo + hi)
    print(f"({lo}, {hi}): f'({m}) = {dfn(m):.2f} ->", "increasing" if dfn(m) > 0 else "decreasing")

xs = np.linspace(-2, 3, 500)
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(xs, fn(xs), 'b-', linewidth=2.5, label=r'$f(x)$')
ax.plot(xs, dfn(xs) / 10, 'g--', linewidth=1.5, label=r"$f^{\prime}(x)/10$")
ax.axvspan(-1, 0, color='green', alpha=0.15, label='Increasing')
ax.axvspan(2, 3, color='green', alpha=0.15)
ax.axvspan(-2, -1, color='red', alpha=0.12, label='Decreasing')
ax.axvspan(0, 2, color='red', alpha=0.12)
ax.axhline(0, color='k', linewidth=0.5)
ax.set_xlabel('$x$')
ax.set_ylim(-30, 60)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper center')

plt.tight_layout()
#If using termux
plt.savefig("figs/Increasing_Function.png")
subprocess.run(shlex.split("termux-open Increasing_Function.png"))
#else
#plt.show()
