import numpy as np

# 1. Verify derivative: d/dx [ (1/3) * arctan(x/3) ] == 1 / (9 + x^2)
x = np.linspace(1.0, 5.0, 10000)
dx = x[1] - x[0]

# Analytical solution function F(x)
F = (1.0 / 3.0) * np.arctan(x / 3.0)

# Numerical derivative using central differences
F_prime = np.gradient(F, dx)

# Expected integrand f(x)
f_expected = 1.0 / (9.0 + x**2)

print("Max derivative error:", np.max(np.abs(F_prime - f_expected)))

# 2. Verify definite integral from 0 to 3 using the trapezoidal rule
a, b = 0.0, 3.0
x_vals = np.linspace(a, b, 10000)
y_vals = 1.0 / (9.0 + x_vals**2)

integral_numeric = np.trapezoid(y_vals, x_vals)
integral_analytic = (1.0 / 3.0) * np.arctan(3.0 / 3.0) - (1.0 / 3.0) * np.arctan(0.0 / 3.0)

print(f"Numerical Integral:  {integral_numeric:.10f}")
print(f"Analytical Integral: {integral_analytic:.10f}")
print(f"Difference:          {abs(integral_numeric - integral_analytic):.2e}")
