# 1.2.7a  Plot f(x) = 3x^4 - 4x^3 - 12x^2 + 5 and f'(x), marking the roots of f'(x) = 0
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 3 * x**4 - 4 * x**3 - 12 * x**2 + 5
df = lambda x: 12 * x**3 - 12 * x**2 - 24 * x
roots = (-1, 0, 2)

x = np.linspace(-2, 3, 500)
plt.figure(figsize=(8, 6))
plt.plot(x, f(x), color='royalblue', label=r'$y=f(x)$')
plt.plot(x, df(x) / 10, color='darkorange', label=r"$y=f^{\prime}(x)/10$")
for r in roots:
    plt.plot(r, 0, 'o', color='crimson', zorder=3)
    plt.annotate(f'({r}, 0)', (r, 0), textcoords="offset points", xytext=(0, 10), ha='center')
plt.axvspan(-1, 0, color='green', alpha=0.12, label='Increasing')
plt.axvspan(2, 3, color='green', alpha=0.12)
plt.axvspan(-2, -1, color='red', alpha=0.10, label='Decreasing')
plt.axvspan(0, 2, color='red', alpha=0.10)
plt.axhline(0, color='k', linewidth=0.5)
plt.title(r'Graph of $f(x)=3x^4-4x^3-12x^2+5$')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-30, 60)
plt.grid(True, alpha=0.4)
plt.legend(loc='upper center')
plt.tight_layout()
plt.savefig('figs/1.2.7a.png')
