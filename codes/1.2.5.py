# 1.2.5  Plane through (a, b, c) parallel to (1 1 1) x = 2
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

def draw_plane(ax, F, e1, e2, s, color, label):
    a, b = np.meshgrid(np.linspace(-s, s, 2), np.linspace(-s, s, 2))
    X = F[:, None, None] + e1[:, None, None] * a + e2[:, None, None] * b
    ax.plot_surface(*X, alpha=0.35, color=color)
    ax.plot([], [], color=color, linewidth=6, alpha=0.5, label=label)

def right_angle(ax, F, u, w, s):
    pts = np.array([F + s * u, F + s * u + s * w, F + s * w])
    ax.plot(*pts.T, 'k-', linewidth=1)

n = np.array([1.0, 1.0, 1.0])
c1 = 2.0
# Assume (a, b, c) = (1, 2, 3).  Then c2 = n^T P0 = a + b + c = 6
P0 = np.array([1.0, 2.0, 3.0])
c2 = n @ P0
F = P0 - (n @ P0 - c1) / (n @ n) * n       # foot of the perpendicular from P0 on the given plane
print("Parallel plane: (1 1 1) x =", c2, "= a + b + c =", P0.sum())
print("Foot on x+y+z=2:", F, ", n^T F =", n @ F)

nh, e1, e2 = plane_basis(n)
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(projection='3d')
draw_plane(ax, F, e1, e2, 3.0, 'tab:blue', r'$x+y+z=2$')
draw_plane(ax, P0, e1, e2, 3.0, 'tab:green', r'$x+y+z=6$')
ax.plot(*np.vstack([F, P0]).T, 'k--', linewidth=1)
ax.quiver(*P0, *(1.6 * nh), color='k', arrow_length_ratio=0.2, linewidth=2)
right_angle(ax, P0, e2, nh, 0.4)
right_angle(ax, F, e2, nh, 0.4)
ax.scatter(*P0, color='r', s=40)
ax.text(*(P0 + 0.3 * e1 - 0.4 * e2), r'$\mathbf{P}_0(1,2,3)$')
ax.text(*(P0 + 1.8 * nh), r'$\mathbf{n}$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_aspect('equal')
view_along_plane(ax, nh, e1)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('figs/1.2.5.png')
