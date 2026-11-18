# 1.2.15a  Distance of P(7,2,4) from the plane through A, B, C
import numpy as np
import matplotlib.pyplot as plt

def row_echelon(M):
    M = M.astype(float).copy()
    m, n = M.shape
    r = 0
    for c in range(n):
        if r == m:
            break
        p = r + np.argmax(np.abs(M[r:, c]))
        if abs(M[p, c]) < 1e-12:
            continue
        M[[r, p]] = M[[p, r]]
        for i in range(r + 1, m):
            M[i] -= M[i, c] / M[r, c] * M[r]
        r += 1
    return M

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

A = np.array([2.0, 5.0, -3.0])
B = np.array([-2.0, -3.0, 5.0])
C = np.array([5.0, 3.0, -3.0])
P = np.array([7.0, 2.0, 4.0])

# Normal n: [(B-A)^T; (C-A)^T] n = 0, solved by elimination with n3 = 4
E = row_echelon(np.vstack([B - A, C - A]))
print("Echelon form:\n", E)
n3 = 4.0
n2 = -E[1, 2] * n3 / E[1, 1]
n1 = -(E[0, 1] * n2 + E[0, 2] * n3) / E[0, 0]
n = np.array([n1, n2, n3])
c = n @ A
d = abs(n @ P - c) / np.linalg.norm(n)
Q = P - (n @ P - c) / (n @ n) * n        # foot of the perpendicular
print("n =", n, ", c =", c, ", n^T B =", n @ B, ", n^T C =", n @ C)
print("Distance =", d, ", sqrt(29) =", np.sqrt(29), ", foot Q =", Q)

nh, e1, e2 = plane_basis(n)
# plane patch around Q that contains A, B and C
coords = np.array([[(X - Q) @ e1, (X - Q) @ e2] for X in (A, B, C)])
lo, hi = coords.min(axis=0) - 1.5, coords.max(axis=0) + 1.5
a, b = np.meshgrid([lo[0], hi[0]], [lo[1], hi[1]])
S = Q[:, None, None] + e1[:, None, None] * a + e2[:, None, None] * b

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(*S, alpha=0.3, color='c')
ax.plot([], [], color='c', linewidth=6, alpha=0.5, label=r'$2x+3y+4z=7$')
ax.plot(*np.vstack([P, Q]).T, 'r--', label=r'$d=\sqrt{29}$ along $\mathbf{n}$')
ax.quiver(*Q, *(2.0 * nh), color='k', arrow_length_ratio=0.2, linewidth=2)
ax.text(*(Q + 1.6 * nh - 0.8 * e2), r'$\mathbf{n}$')
right_angle(ax, Q, e2, nh, 0.8)
for X, lab in ((A, 'A'), (B, 'B'), (C, 'C'), (P, 'P'), (Q, 'Q')):
    ax.scatter(*X, color='r' if lab in 'PQ' else 'k', s=30)
    off = -0.9 * e2 - 0.3 * nh if lab == 'Q' else 0.6 * e2 + 0.3 * nh
    ax.text(*(X + off), rf'$\mathbf{{{lab}}}$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_aspect('equal')
view_along_plane(ax, nh, e1)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('figs/1.2.15a.png', dpi=200, bbox_inches='tight', pad_inches=0.05)
