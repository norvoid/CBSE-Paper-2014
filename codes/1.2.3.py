# 1.2.3  Projection of a = (1,3,7) on b = (2,-3,6)
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 3, 7])
b = np.array([2, -3, 6])
proj = a @ b / np.linalg.norm(b)
p = (a @ b / (b @ b)) * b              # projection vector
print("Scalar projection a^T b/||b|| =", proj)
print("Projection vector             =", p, ", norm =", np.linalg.norm(p))
print("(a - p)^T b                   =", (a - p) @ b)

O = np.zeros(3)
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(projection='3d')
for v, col, lab in ((a, 'b', r'$\mathbf{a}$'), (b, 'g', r'$\mathbf{b}$'),
                    (p, 'r', r'$\frac{\mathbf{a}^{\top}\mathbf{b}}{\|\mathbf{b}\|^2}\mathbf{b}$')):
    ax.plot(*np.vstack([O, v]).T, color=col, linewidth=2)
    ax.scatter(*v, color=col, s=25)
    ax.text(*(v + np.array([0.15, 0, 0.2])), lab, color=col)
ax.plot(*np.vstack([a, p]).T, 'k--', label=r'$\mathbf{a}-\mathbf{p}\perp\mathbf{b}$')
ax.set_xlim(0, 3)
ax.set_ylim(-4, 4)
ax.set_zlim(0, 8)
ax.view_init(elev=20, azim=-35)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('figs/1.2.3.png', dpi=200, bbox_inches='tight', pad_inches=0.05)
