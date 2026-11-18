# 1.2.10b  a + b + c = 0, ||a|| = 3, ||b|| = 5, ||c|| = 7: angle between a and b
import numpy as np
import matplotlib.pyplot as plt

# a, b, c lie in a plane.  Assume a = (3, 0).
# a^T b = (||c||^2 - ||a||^2 - ||b||^2)/2 = 15/2  ->  3 b1 = 15/2  ->  b1 = 5/2
# ||b|| = 5  ->  b2 = sqrt(25 - b1^2) = 5 sqrt(3)/2,   c = -(a + b)
a = np.array([3.0, 0.0])
dot = (49 - 9 - 25) / 2
b1 = dot / a[0]
b = np.array([b1, np.sqrt(25 - b1**2)])
c = -(a + b)
print("b =", b, ", c =", c)
print("||a||, ||b||, ||c|| =", np.linalg.norm(a), np.linalg.norm(b), np.linalg.norm(c))
theta = np.arccos(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))
print("theta =", theta, "= pi/3:", np.isclose(theta, np.pi / 3))

plt.figure(figsize=(7, 6))
O = np.zeros(2)
plt.quiver(*O, *a, angles='xy', scale_units='xy', scale=1, color='b', label=r'$\mathbf{a}$')
plt.quiver(*a, *b, angles='xy', scale_units='xy', scale=1, color='g', label=r'$\mathbf{b}$ (head to tail)')
plt.quiver(*(a + b), *c, angles='xy', scale_units='xy', scale=1, color='r', label=r'$\mathbf{c}=-(\mathbf{a}+\mathbf{b})$')
plt.quiver(*O, *b, angles='xy', scale_units='xy', scale=1, color='g', alpha=0.4, label=r'$\mathbf{b}$ from origin')
arc = np.linspace(0, theta, 50)
plt.plot(0.8 * np.cos(arc), 0.8 * np.sin(arc), 'm-')
plt.text(0.9, 0.35, r'$\theta=\frac{\pi}{3}$', color='m')
plt.xlim(-1, 6.5)
plt.ylim(-1, 5.5)
plt.gca().set_aspect('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('figs/1.2.10b.png', dpi=200, bbox_inches='tight', pad_inches=0.05)
