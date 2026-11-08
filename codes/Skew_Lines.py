import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Lines  x = A1 + lam m1  and  x = A2 + mu m2
A1 = np.array([-1.0, -3.0, -5.0]).reshape(-1, 1)
m1 = np.array([3.0, 5.0, 7.0]).reshape(-1, 1)
A2 = np.array([2.0, 4.0, 6.0]).reshape(-1, 1)
m2 = np.array([1.0, 3.0, 5.0]).reshape(-1, 1)

# Intersection condition: [m1  -m2] [lam; mu] = A2 - A1
M = np.block([m1, -m2])
b = A2 - A1
Mb = np.block([M, b])
print("rank(M)  =", np.linalg.matrix_rank(M))
print("rank(Mb) =", np.linalg.matrix_rank(Mb))

sol, res, rk, sv = np.linalg.lstsq(M, b, rcond=None)
lam, mu = sol.flatten()
print("lambda, mu =", lam, mu)
print("Residual   =", np.linalg.norm(M @ sol - b))

P = A1 + lam * m1
print("Point of intersection:", P.flatten())
print("Check on line 2      :", (A2 + mu * m2).flatten())

# 3D plot
t = np.linspace(-1.5, 2.0, 50)
L1 = A1 + m1 * t
L2 = A2 + m2 * t
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
ax.plot(L1[0], L1[1], L1[2], 'b-', label=r'Line 1')
ax.plot(L2[0], L2[1], L2[2], 'g-', label=r'Line 2')
ax.plot(P[0], P[1], P[2], 'ro', markersize=8, label='Intersection')
ax.text(P[0, 0], P[1, 0], P[2, 0] + 0.8, r'$\left(\frac{1}{2}, -\frac{1}{2}, -\frac{3}{2}\right)$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc='upper left')

plt.tight_layout()
#If using termux
plt.savefig("figs/Skew_Lines.png")
subprocess.run(shlex.split("termux-open Skew_Lines.png"))
#else
#plt.show()
