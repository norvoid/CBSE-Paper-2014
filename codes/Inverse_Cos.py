import numpy as np
import matplotlib.pyplot as plt

# 1. Numerical Verification of the Solution
# Define a fine range of x values in the valid domain [0, 1]
x_vals = np.linspace(0.0, 1.0, 1000)

# Calculate LHS: sin(arcsin(1/5) + arccos(x))
lhs_vals = np.sin(np.arcsin(1/5) + np.arccos(x_vals))

# Find where LHS is approximately equal to 1 (within small tolerance)
tolerance = 1e-5
solution_indices = np.where(np.abs(lhs_vals - 1.0) < tolerance)
approx_solution = x_vals[solution_indices]

print(f"Exact theoretical solution: x = 1/5 or 0.2")
print(f"Numerically verified solution points near x = 0.2: {approx_solution}")

# 2. Matplotlib Visualization
plt.figure(figsize=(8, 6))
plt.plot(x_vals, lhs_vals, label=r'$\sin\left(\sin^{-1}\left(\frac{1}{5}\right) + \cos^{-1}(x)\right)$', color='blue', linewidth=2)
plt.axhline(y=1, color='red', linestyle='--', label='Target Value ($y = 1$)')
plt.axvline(x=0.2, color='green', linestyle=':', label='Solution ($x = 0.2$ or $1/5$)')

plt.title('Verification of Inverse Trigonometric Equation')
plt.xlabel('x')
plt.ylabel(r'$\sin\left(\sin^{-1}\left(\frac{1}{5}\right) + \cos^{-1}(x)\right)$')
plt.grid(True)
plt.legend()

# Save the generated graph as a PNG image
plt.savefig('Inverse_Cos.png', dpi=300, bbox_inches='tight')

# Uncomment below to display the plot interactively if running in a desktop GUI environment
# plt.show()
