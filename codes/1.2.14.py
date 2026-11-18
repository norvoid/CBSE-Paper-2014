# 1.2.14  Integral from pi/6 to pi/3 of 1/(1 + sqrt(cot x)) by the trapezoidal rule
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 1 / (1 + np.sqrt(1 / np.tan(x)))
a, b = np.pi / 6, np.pi / 3

def trapz(n):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    return h / 2 * (f(x[0]) + 2 * np.sum(f(x[1:-1])) + f(x[-1]))

for n in (1, 2, 4, 16, 1000):
    print(f"T_{n} = {trapz(n):.10f}")
print("pi/12 =", f"{np.pi / 12:.10f}")

n = 4
xk = np.linspace(a, b, n + 1)
xs = np.linspace(a, b, 300)
plt.figure(figsize=(7, 5))
plt.plot(xs, f(xs), color='royalblue', label=r'$y=\frac{1}{1+\sqrt{\cot x}}$')
plt.fill_between(xk, f(xk), color='darkorange', alpha=0.3, label=f'Trapezoids, $n={n}$')
plt.plot(xk, f(xk), 'o', color='crimson')
for xv in xk:
    plt.plot([xv, xv], [0, f(xv)], color='darkorange', linewidth=0.8)
plt.title(r'Trapezoidal rule for $\int_{\pi/6}^{\pi/3}\frac{dx}{1+\sqrt{\cot x}}$')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0, 0.7)
plt.grid(True, alpha=0.4)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('figs/1.2.14.png', dpi=200, bbox_inches='tight', pad_inches=0.05)
