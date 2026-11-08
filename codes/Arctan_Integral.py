import numpy as np
from scipy.integrate import quad

# Integral of 1/(9+x^2) from 0 to infinity
f = lambda x: 1.0 / (9.0 + x**2)
val, err = quad(f, 0, np.inf)
print("Numerical value :", val)
print("pi/6            :", np.pi / 6)

# Antiderivative F(x) = (1/3) arctan(x/3)
F = lambda x: np.arctan(x / 3.0) / 3.0
print("F(b)-F(0), b=1e6:", F(1e6) - F(0.0))
