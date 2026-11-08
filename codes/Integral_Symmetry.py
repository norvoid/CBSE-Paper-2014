import numpy as np
from scipy.integrate import quad

f = lambda x: 1.0 / (1.0 + np.sqrt(1.0 / np.tan(x)))          # 1/(1+sqrt(cot x))
g = lambda x: f(np.pi / 2 - x)                                # reflected integrand

a, b = np.pi / 6, np.pi / 3
I, _ = quad(f, a, b)
J, _ = quad(g, a, b)
print("I      =", I)
print("pi/12  =", np.pi / 12)
print("I + J  =", I + J, ", b - a =", b - a)
