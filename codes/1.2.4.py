# 1.2.4  Unit vectors a, b with a + b a unit vector: angle between a and b
import numpy as np
import matplotlib.pyplot as plt

# Assume a = (1, 0).  From ||a + b||^2 = 1:  a^T b = -1/2  ->  b1 = -1/2,
# and ||b|| = 1  ->  b2 = sqrt(1 - b1^2) = sqrt(3)/2
a = np.array([1.0, 0.0])
b1 = -0.5
b2 = np.sqrt(1 - b1**2)
b = np.array([b1, b2])
s = a + b
theta = np.arccos(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))
print("b =", b)
print("||a||, ||b||, ||a+b|| =", np.linalg.norm(a), np.linalg.norm(b), np.linalg.norm(s))
print("a^T b =", a @ b, ", theta =", theta, "= 2pi/3:", np.isclose(theta, 2 * np.pi / 3))

t = np.linspace(0, 2 * np.pi, 300)
plt.figure(figsize=(6, 6))
plt.plot(np.cos(t), np.sin(t), 'k:', label='Unit circle')
for v, col, lab in ((a, 'b', r'$\mathbf{a}$'), (b, 'g', r'$\mathbf{b}$'), (s, 'r', r'$\mathbf{a}+\mathbf{b}$')):
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=col, label=lab)
plt.plot([a[0], s[0]], [a[1], s[1]], 'g--', alpha=0.6)
plt.plot([b[0], s[0]], [b[1], s[1]], 'b--', alpha=0.6)
arc = np.linspace(0, theta, 50)
plt.plot(0.25 * np.cos(arc), 0.25 * np.sin(arc), 'm-')
plt.text(0.05, 0.3, r'$\theta=\frac{2\pi}{3}$', color='m')
plt.xlim(-1.3, 1.3)
plt.ylim(-1.3, 1.3)
plt.gca().set_aspect('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower left')
plt.tight_layout()
plt.savefig('figs/1.2.4.png')
