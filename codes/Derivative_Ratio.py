import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# u = tan^{-1}(sqrt(1-x^2)/x),  v = cos^{-1}(2x sqrt(1-x^2))
x = sp.symbols('x', real=True)
u = sp.atan(sp.sqrt(1 - x**2) / x)
v = sp.acos(2 * x * sp.sqrt(1 - x**2))
du = sp.lambdify(x, sp.diff(u, x), 'numpy')
dv = sp.lambdify(x, sp.diff(v, x), 'numpy')

# Sample points in (-1,1) excluding x = 0 and x = +-1/sqrt(2)
xs = np.concatenate((np.linspace(-0.99, -0.01, 400), np.linspace(0.01, 0.99, 400)))
xs = xs[np.abs(np.abs(xs) - 1 / np.sqrt(2)) > 0.01]
ratio = du(xs) / dv(xs)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(xs, ratio, 'b.', markersize=3, label=r'$\frac{du}{dv}$')
ax.axvline(1 / np.sqrt(2), color='r', linestyle='--', alpha=0.6)
ax.axvline(-1 / np.sqrt(2), color='r', linestyle='--', alpha=0.6)
ax.set_xlabel('$x$')
ax.set_ylabel(r'$\frac{du}{dv}$')
ax.set_ylim(-1, 1)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')

print("du/dv for |x| < 1/sqrt(2):", np.unique(np.round(ratio[np.abs(xs) < 1 / np.sqrt(2) - 0.01], 6)))
print("du/dv for |x| > 1/sqrt(2):", np.unique(np.round(ratio[np.abs(xs) > 1 / np.sqrt(2) + 0.01], 6)))

plt.tight_layout()
#If using termux
plt.savefig("figs/Derivative_Ratio.png")
subprocess.run(shlex.split("termux-open Derivative_Ratio.png"))
#else
#plt.show()
