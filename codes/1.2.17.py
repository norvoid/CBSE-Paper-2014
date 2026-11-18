# 1.2.17  Lost card: Y ~ Bernoulli(1/4) (1 = spade lost), X | Y ~ Hypergeometric(51, 13 - Y, 3)
import numpy as np
import matplotlib.pyplot as plt
from math import comb
from fractions import Fraction

pY = {0: Fraction(3, 4), 1: Fraction(1, 4)}

def pX_given_Y(k, y):
    return Fraction(comb(13 - y, k) * comb(38 + y, 3 - k), comb(51, 3))

k = np.arange(4)
pX = [sum(pX_given_Y(j, y) * pY[y] for y in (0, 1)) for j in k]
post = {y: pX_given_Y(3, y) * pY[y] / pX[3] for y in (0, 1)}
print("p_X(k) =", [str(p) for p in pX], "=", [float(p) for p in pX])
print("p_{Y|X}(1|3) =", post[1], "=", float(post[1]))

rng = np.random.default_rng(0)
N = 10_000_000
Y = (rng.random(N) < 13 / 52).astype(int)
X = rng.hypergeometric(13 - Y, 38 + Y, 3)      # spades among 3 cards from the 51 left
sim_pX = np.bincount(X, minlength=4) / N
sel = X == 3
sim_post = np.bincount(Y[sel], minlength=2) / sel.sum()
print("Simulated p_X(k)       =", sim_pX)
print("Simulated p_{Y|X}(1|3) =", sim_post[1], f"({sel.sum()} trials with three spades)")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].stem(k - 0.05, [float(p) for p in pX], linefmt='b-', markerfmt='bo', basefmt=' ', label='Theory')
ax[0].stem(k + 0.05, sim_pX, linefmt='r--', markerfmt='rs', basefmt=' ', label='Simulation')
ax[0].set_title(r'$p_X(k)$')
ax[0].set_xlabel('$k$ (spades drawn)')
ax[0].set_xticks(k)
y = np.arange(2)
ax[1].stem(y - 0.03, [float(post[0]), float(post[1])], linefmt='b-', markerfmt='bo', basefmt=' ', label='Theory')
ax[1].stem(y + 0.03, sim_post, linefmt='r--', markerfmt='rs', basefmt=' ', label='Simulation')
ax[1].set_title(r'$p_{Y|X}(y|3)$')
ax[1].set_xlabel('$y$ (1 = lost card is a spade)')
ax[1].set_xticks(y)
for a in ax:
    a.set_ylim(0, 1)
    a.grid(True, linestyle='--', alpha=0.5)
    a.legend()
plt.tight_layout()
plt.savefig('figs/1.2.17.png', dpi=200, bbox_inches='tight', pad_inches=0.05)
