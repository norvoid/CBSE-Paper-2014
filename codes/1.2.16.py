# 1.2.16  LPP: maximise Z = 22x + 18y s.t. 3x + 2y <= 48, x + y <= 20, x, y >= 0
import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

c = np.array([22.0, 18.0])
G = np.array([[3.0, 2.0], [1.0, 1.0]])
h = np.array([48.0, 20.0])

# Optimisation with cvxpy
v = cp.Variable(2)
prob = cp.Problem(cp.Maximize(c @ v), [G @ v <= h, v >= 0])
prob.solve()
x_opt = v.value
print("cvxpy optimum:", np.round(x_opt, 4), ", maximum profit:", round(prob.value, 4))

# Vertex B where both constraints are tight, by Gaussian elimination:
# R2 -> 3R2 - R1 gives [0 1 | 12], then 3x = 48 - 2y
M = np.column_stack([G, h])
M[1] = 3 * M[1] - M[0]
y = M[1, 2] / M[1, 1]
x = (M[0, 2] - M[0, 1] * y) / M[0, 0]
print("Echelon form:\n", M, f"\nVertex B = ({x:g}, {y:g})")

O = np.zeros((2, 1))
Av = np.array([[16.0], [0.0]])
Bv = np.array([[x], [y]])
Cv = np.array([[0.0], [20.0]])
V = np.block([O, Av, Bv, Cv])
for i, lab in enumerate("OABC"):
    print(lab, V[:, i], "Z =", c @ V[:, i])

fig, ax = plt.subplots(figsize=(8, 7))
ax.fill(V[0, :], V[1, :], color='skyblue', alpha=0.5, label='Feasible region')
for P1, P2, lab in ((np.array([[0.0], [24.0]]), Av, r'$3x+2y=48$'),
                    (np.array([[0.0], [20.0]]), np.array([[20.0], [0.0]]), r'$x+y=20$')):
    xl = line_gen(P1, P2)
    ax.plot(xl[0, :], xl[1, :], linewidth=2, label=lab)
Z = prob.value
iso = line_gen(np.array([[0.0], [Z / 18.0]]), np.array([[Z / 22.0], [0.0]]))
ax.plot(iso[0, :], iso[1, :], 'r--', linewidth=1.5, label=r'$22x+18y=392$')
ax.plot(x_opt[0], x_opt[1], 'r*', markersize=14, label='cvxpy optimum')
ax.plot(V[0, :], V[1, :], 'ko')
label_pts(V, [r'$O(0,0)$', r'$A(16,0)$', r'$B(8,12)$', r'$C(0,20)$'])
ax.set_xlabel('Electronic machines $x$')
ax.set_ylabel('Manual machines $y$')
ax.set_xlim(-1, 22)
ax.set_ylim(-1, 26)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('figs/1.2.16.png', dpi=200, bbox_inches='tight', pad_inches=0.05)
