# 1.2.7b  Tangent and normal to x = a sin^3 t, y = a cos^3 t at t = pi/4
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Assume a = 2.  Then P = r(pi/4) = (a/(2 sqrt2)) (1, 1) = (1/sqrt2)(1, 1)
a = 2.0
r = lambda t: a * np.array([np.sin(t)**3, np.cos(t)**3])
dr = lambda t: 3 * a * np.sin(t) * np.cos(t) * np.array([np.sin(t), -np.cos(t)])
t0 = np.pi / 4
P = r(t0)
t = dr(t0)                              # tangent direction
n = np.array([[0, -1], [1, 0]]) @ t     # rotate by 90 degrees: n^T t = 0
print("P =", P, ", t =", t, ", n =", n, ", n^T t =", n @ t)
print("Tangent: n^T x = n^T P ->", n / n[0], "x =", (n @ P) / n[0], "= a/sqrt2 =", a / np.sqrt(2))
print("Normal : t^T x = t^T P ->", t / t[0], "x =", (t @ P) / t[0])

th = np.linspace(0, np.pi / 2, 300)
C = np.array([r(s) for s in th]).T
x_T = line_gen(np.array([[0.0], [a / np.sqrt(2)]]), np.array([[a / np.sqrt(2)], [0.0]]))
x_N = line_gen(np.array([[0.0], [0.0]]), np.array([[a], [a]]))
plt.figure(figsize=(7, 7))
plt.plot(C[0], C[1], 'b-', linewidth=2, label='Curve ($a=2$)')
plt.plot(x_T[0, :], x_T[1, :], 'r-', label=r'Tangent: $x+y=\frac{a}{\sqrt{2}}$')
plt.plot(x_N[0, :], x_N[1, :], 'g--', label=r'Normal: $x-y=0$')
plt.plot(P[0], P[1], 'ko')
label_pts(P.reshape(-1, 1), [r'$\mathbf{P}$'])
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(-0.2, 2.4)
plt.ylim(-0.2, 2.4)
plt.gca().set_aspect('equal')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('figs/1.2.7b.png')
