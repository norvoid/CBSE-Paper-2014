import numpy as np
from scipy.integrate import solve_ivp

# e^x sqrt(1-y^2) dx + (y/x) dy = 0, y(0) = 1
# Solution: sqrt(1-y^2) = (x-1) e^x + 1
z_exact = lambda x: (x - 1) * np.exp(x) + 1.0
y_exact = lambda x: np.sqrt(1 - z_exact(x)**2)

# With z = sqrt(1-y^2): z dz = -y dy, so dz/dx = x e^x, z(0) = 0
sol = solve_ivp(lambda x, z: x * np.exp(x) * np.ones_like(z), [0, 0.5], [0.0],
                t_eval=np.linspace(0, 0.5, 6), rtol=1e-10, atol=1e-12)
print("x      :", sol.t)
print("z (num):", sol.y[0])
print("z exact:", z_exact(sol.t))
print("y exact:", y_exact(sol.t))
print("y(0) =", y_exact(0.0))
