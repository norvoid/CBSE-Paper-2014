# 1.2.2  Plot y = 2x^2 - 40 and y = 32, marking their intersections
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 400)
roots = (-6, 6)

plt.figure(figsize=(7, 5))
plt.plot(x, 2 * x**2 - 40, color='royalblue', label=r'$y=2x^2-40$')
plt.axhline(32, color='darkorange', label=r'$y=32$')
for r in roots:
    plt.plot(r, 32, 'o', color='crimson', zorder=3)
    plt.annotate(f'({r}, 32)', (r, 32), textcoords="offset points", xytext=(0, 10), ha='center')
plt.title(r'Graph of $2x^2-40=32$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, alpha=0.4)
plt.legend(loc='lower left')
plt.tight_layout()
plt.savefig('figs/1.2.2.png')
