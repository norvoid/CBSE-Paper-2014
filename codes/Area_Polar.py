import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad
#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

R = np.sqrt(32.0)

# Area by double integral in polar coordinates: int int r dr dtheta
area, _ = dblquad(lambda r, th: r, 0, np.pi / 4, lambda th: 0.0, lambda th: R)
print("Area =", area, ", 4 pi =", 4 * np.pi)

# Vertices of the region
O = np.array([0.0, 0.0]).reshape(-1, 1)
P = np.array([4.0, 4.0]).reshape(-1, 1)
Q = np.array([R, 0.0]).reshape(-1, 1)

fig, ax = plt.subplots(figsize=(7, 7))
th = np.linspace(0, np.pi / 4, 200)
x_arc = R * np.cos(th)
y_arc = R * np.sin(th)
x_OP = line_gen(O, P)
x_OQ = line_gen(O, Q)

ax.fill(np.concatenate(([0.0], x_arc)), np.concatenate(([0.0], y_arc)), color='skyblue', alpha=0.5)
ax.plot(x_OP[0, :], x_OP[1, :], 'k-', linewidth=2, label=r'$y=x$')
ax.plot(x_OQ[0, :], x_OQ[1, :], 'k-', linewidth=2, label=r'$x$-axis')
ax.plot(R * np.cos(np.linspace(0, np.pi / 2, 200)), R * np.sin(np.linspace(0, np.pi / 2, 200)),
        'r--', linewidth=1.5, label=r'$x^2+y^2=32$')
V = np.block([O, P, Q])
ax.plot(V[0, :], V[1, :], 'ko')
label_pts(V, [r'$O$', r'$P(4,4)$', r'$Q(4\sqrt{2},0)$'])
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-0.5, 6.5)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')

plt.tight_layout()
#If using termux
plt.savefig("figs/Area_Polar.png")
subprocess.run(shlex.split("termux-open Area_Polar.png"))
#else
#plt.show()
