import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Cone of slant height l = 1:  r = sin(alpha), h = cos(alpha)
l = 1.0
alpha = np.linspace(0, np.pi / 2, 500)
V = np.pi / 3 * (l * np.sin(alpha))**2 * (l * np.cos(alpha))

a_opt = alpha[np.argmax(V)]
print("Numerical alpha* =", a_opt)
print("arccos(1/sqrt(3)) =", np.arccos(1 / np.sqrt(3)))
print("Vmax numerical    =", V.max(), ", 2 pi / (9 sqrt(3)) =", 2 * np.pi / (9 * np.sqrt(3)))

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(alpha, V, 'b-', linewidth=2.5, label=r'$V\left(\alpha\right)$')
ax.plot([np.arccos(1 / np.sqrt(3))], [V.max()], 'ro', markersize=8)
ax.annotate(r'$\alpha=\cos^{-1}\frac{1}{\sqrt{3}}$', (np.arccos(1 / np.sqrt(3)), V.max()),
            textcoords="offset points", xytext=(0, 12), ha='center')
ax.set_xlabel(r'$\alpha$ (rad)')
ax.set_ylabel('$V$ (for $l=1$)')
ax.set_ylim(0, 0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='lower center')

plt.tight_layout()
#If using termux
plt.savefig("figs/Cone_Volume.png")
subprocess.run(shlex.split("termux-open Cone_Volume.png"))
#else
#plt.show()
