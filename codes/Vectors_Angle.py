import matplotlib.pyplot as plt
import numpy as np

# 1. Define vectors in 3D space
# Let vector a lie along the x-axis: a = [1, 0, 0]
a = np.array([1.0, 0.0, 0.0])

# Vector b at an angle of 120 degrees (2pi/3) in the xy-plane from vector a
theta = 2 * np.pi / 3  #[cite: 2]
b = np.array([np.cos(theta), np.sin(theta), 0.0])

# Resultant vector
sum_ab = a + b

# 2. Verification Calculations
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)
norm_sum = np.linalg.norm(sum_ab)
dot_product = np.dot(a, b)
calculated_theta = np.arccos(dot_product / (norm_a * norm_b))

print('--- 3D Vector Verification Results ---')
print(f'Norm of vector a: {norm_a:.4f} (Expected: 1.0)')
print(f'Norm of vector b: {norm_b:.4f} (Expected: 1.0)')
print(f'Norm of vector a + b: {norm_sum:.4f} (Expected: 1.0)')
print(f'Dot product (a^T * b): {dot_product:.4f} (Expected: -0.5)')  #[cite: 2]
print(
    f'Calculated angle theta: {np.degrees(calculated_theta):.2f}° '
    f'({calculated_theta:.4f} rad / Expected: 120° or 2pi/3)'
)  #[cite: 2]

# 3. 3D Matplotlib Visualization
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')

# Origin point for vectors
origin = np.array([0, 0, 0])

# Plot vectors using quiver
ax.quiver(
    *origin,
    *a,
    color='red',
    length=1.0,
    normalize=False,
    arrow_length_ratio=0.1,
    label=r'$\mathbf{a}$',
)
ax.quiver(
    *origin,
    *b,
    color='blue',
    length=1.0,
    normalize=False,
    arrow_length_ratio=0.1,
    label=r'$\mathbf{b}$',
)
ax.quiver(
    *origin,
    *sum_ab,
    color='green',
    length=1.0,
    normalize=False,
    arrow_length_ratio=0.1,
    label=r'$\mathbf{a} + \mathbf{b}$',
)

# Plot an arc/curve to visually represent the angle theta between vector a and b
arc_theta = np.linspace(0, theta, 50)
arc_radius = 0.4
arc_x = arc_radius * np.cos(arc_theta)
arc_y = arc_radius * np.sin(arc_theta)
arc_z = np.zeros_like(arc_theta)
ax.plot(
    arc_x,
    arc_y,
    arc_z,
    color='purple',
    linestyle='--',
    linewidth=2,
    label=r'$\theta = \frac{2\pi}{3}$',
)

# Label vectors on the plot
ax.text(
    a[0] * 0.5 + 0.1, a[1] * 0.5, a[2] * 0.5, r'$\mathbf{a}$', color='red', fontsize=12
)
ax.text(
    b[0] * 0.5 - 0.2,
    b[1] * 0.5 + 0.1,
    b[2] * 0.5,
    r'$\mathbf{b}$',
    color='blue',
    fontsize=12,
)
ax.text(
    sum_ab[0] * 0.5 + 0.1,
    sum_ab[1] * 0.5 + 0.1,
    sum_ab[2] * 0.5,
    r'$\mathbf{a} + \mathbf{b}$',
    color='green',
    fontsize=12,
)

# Text annotation for the angle arc
ax.text(
    0.3,
    0.3,
    0.05,
    r'$\theta = 120^\circ$',
    color='purple',
    fontsize=11,
    weight='bold',
)

# Set limits and labels
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])
ax.set_zlim([-1.2, 1.2])
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Title using standard mathtext notation compatible with Matplotlib
ax.set_title(
    r'3D Verification: $\|\mathbf{a}\| = \|\mathbf{b}\| = \|\mathbf{a}+\mathbf{b}\| '
    r'= 1 \Rightarrow \theta = \frac{2\pi}{3}$',
    fontsize=11,
)

ax.legend(loc='upper left')

# Save the figure before showing it
plt.savefig('Vectors_Angle.png', dpi=300, bbox_inches='tight')
print("Plot successfully saved as 'Vectors_Angle.png'")

plt.show()
