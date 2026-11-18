# 1.2.9  (x^2-1) y' + 2xy = 2/(x^2-1):  y = (ln|(x-1)/(x+1)| + C)/(x^2-1)
import numpy as np

y = lambda x, C: (np.log(np.abs((x - 1) / (x + 1))) + C) / (x**2 - 1)
h = 1e-6
xs_all = np.concatenate((np.linspace(-4, -1.05, 200), np.linspace(-0.95, 0.95, 200),
                         np.linspace(1.05, 4, 200)))
for C in (-1.0, 0.0, 2.0):
    dy = (y(xs_all + h, C) - y(xs_all - h, C)) / (2 * h)
    res = (xs_all**2 - 1) * dy + 2 * xs_all * y(xs_all, C) - 2 / (xs_all**2 - 1)
    print(f"C = {C}: max |residual| = {np.max(np.abs(res)):.2e}")
