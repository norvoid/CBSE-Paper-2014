import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Maximise Z = 22 x + 18 y
c = np.array([22.0, 18.0]).reshape(-1, 1)
G = np.array([[360.0, 240.0],
              [1.0, 1.0]])
h = np.array([5760.0, 20.0])

v = cp.Variable((2, 1))
prob = cp.Problem(cp.Maximize(c.T @ v), [G @ v <= h.reshape(-1, 1), v >= 0])
prob.solve()
print("Optimal point:", np.round(v.value.flatten(), 4))
print("Maximum profit:", round(prob.value, 4))

# Corner points of the feasible region
O = np.array([0.0, 0.0]).reshape(-1, 1)
A = np.array([16.0, 0.0]).reshape(-1, 1)
B = np.array([8.0, 12.0]).reshape(-1, 1)
C = np.array([0.0, 20.0]).reshape(-1, 1)
V = np.block([O, A, B, C])
for i, lab in enumerate("OABC"):
    print(lab, V[:, i], "Z =", (c.T @ V[:, i].reshape(-1, 1)).item())

fig, ax = plt.subplots(figsize=(8, 7))
ax.fill(V[0, :], V[1, :], color='skyblue', alpha=0.5, label='Feasible region')
for P1, P2, lab in ((np.array([[0.0], [24.0]]), A, r'$3x+2y=48$'),
                    (np.array([[0.0], [20.0]]), np.array([[20.0], [0.0]]), r'$x+y=20$')):
    xl = line_gen(P1, P2)
    ax.plot(xl[0, :], xl[1, :], linewidth=2, label=lab)
iso = line_gen(np.array([[0.0], [392.0 / 18.0]]), np.array([[392.0 / 22.0], [0.0]]))
ax.plot(iso[0, :], iso[1, :], 'r--', linewidth=1.5, label=r'$22x+18y=392$')
ax.plot(V[0, :], V[1, :], 'ko')
label_pts(V, [r'$O(0,0)$', r'$A(16,0)$', r'$B(8,12)$', r'$C(0,20)$'])
ax.set_xlabel('Electronic machines $x$')
ax.set_ylabel('Manual machines $y$')
ax.set_xlim(-1, 22)
ax.set_ylim(-1, 26)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')

plt.tight_layout()
#If using termux
plt.savefig("figs/LPP.png")
subprocess.run(shlex.split("termux-open LPP.png"))
#else
#plt.show()
