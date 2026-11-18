# 1.2.8  e^x sqrt(1-y^2) dx + (y/x) dy = 0, y(0) = 1:  sqrt(1-y^2) = (x-1)e^x + 1
import numpy as np
import matplotlib.pyplot as plt

z = lambda x: (x - 1) * np.exp(x) + 1          # z = sqrt(1 - y^2)

# Residual of the differential equation for 0 < x < 1
x = np.linspace(0.05, 0.95, 50)
y = lambda x: np.sqrt(1 - z(x)**2)
h = 1e-6
dy = (y(x + h) - y(x - h)) / (2 * h)
res = np.exp(x) * np.sqrt(1 - y(x)**2) + y(x) / x * dy
print("max |residual| =", np.max(np.abs(res)), ", y(0) =", y(0.0))

xs = np.linspace(-4, 1, 400)
plt.figure(figsize=(7, 5))
plt.plot(xs, y(xs), 'b-', linewidth=2, label=r'$y=\sqrt{1-\left((x-1)e^x+1\right)^2}$')
plt.plot(0, 1, 'ro')
plt.annotate(r'$(0,1)$', (0, 1), textcoords="offset points", xytext=(0, -18), ha='center')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower left')
plt.tight_layout()
plt.savefig('figs/1.2.8.png')
