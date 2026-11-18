# 1.2.15b  Distance of P(-1,-5,-10) from the intersection of a line and a plane
import numpy as np
import matplotlib.pyplot as plt

def plane_basis(n):
    """Unit normal nh, a horizontal in-plane unit vector e1 and the in-plane unit vector e2 ⟂ e1."""
    nh = n / np.linalg.norm(n)
    e1 = np.array([nh[1], -nh[0], 0.0])
    e1 = e1 / np.linalg.norm(e1) if np.linalg.norm(e1) > 1e-12 else np.array([1.0, 0.0, 0.0])
    e2 = np.array([0.0, 0.0, 1.0]) - nh[2] * nh - e1[2] * e1
    return nh, e1, e2 / np.linalg.norm(e2)

def view_along_plane(ax, nh, e1, tilt=25):
    """Look along the in-plane line e1, tilted towards the normal, with an orthographic camera."""
    t = np.radians(tilt)
    v = np.cos(t) * e1 + np.sin(t) * nh
    ax.view_init(elev=np.degrees(np.arcsin(v[2])), azim=np.degrees(np.arctan2(v[1], v[0])))
    ax.set_proj_type('ortho')

def right_angle(ax, F, u, w, s):
    pts = np.array([F + s * u, F + s * u + s * w, F + s * w])
    ax.plot(*pts.T, 'k-', linewidth=1)

A = np.array([2.0, -1.0, 2.0])
m = np.array([3.0, 4.0, 2.0])
n = np.array([1.0, -1.0, 1.0])
c = 5.0
P = np.array([-1.0, -5.0, -10.0])

lam = (c - n @ A) / (n @ m)
Q = A + lam * m
print("lambda =", lam, ", Q =", Q, ", n^T Q =", n @ Q)
print("||P - Q|| =", np.linalg.norm(P - Q))

nh, e1, e2 = plane_basis(n)
a, b = np.meshgrid([-8, 8], [-8, 8])
S = Q[:, None, None] + e1[:, None, None] * a + e2[:, None, None] * b

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(*S, alpha=0.3, color='c')
ax.plot([], [], color='c', linewidth=6, alpha=0.5, label=r'$x-y+z=5$')
t = np.linspace(-2.5, 2.5, 20)
L = A[:, None] + m[:, None] * t
ax.plot(*L, 'b-', linewidth=2, label='Line')
ax.quiver(*Q, *(4 * nh), color='k', arrow_length_ratio=0.15, linewidth=2)
ax.text(*(Q + 4.4 * nh), r'$\mathbf{n}$')
right_angle(ax, Q, e2, nh, 1.0)
ax.scatter(*Q, color='k', s=40)
ax.text(*(Q + 0.6 * nh - 1.6 * e2), r'$\mathbf{Q}(2,-1,2)$')
ax.scatter(*P, color='r', s=40)
ax.text(*(P - 2.6 * nh), r'$\mathbf{P}(-1,-5,-10)$')
ax.plot(*np.vstack([P, Q]).T, 'r--', label=r'$\|\mathbf{P}-\mathbf{Q}\|=13$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_aspect('equal')
view_along_plane(ax, nh, e1)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('figs/1.2.15b.png', dpi=200, bbox_inches='tight', pad_inches=0.05)
