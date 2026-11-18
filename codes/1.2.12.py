# 1.2.12  Two children, X1 (elder), X2 (younger) ~ Bernoulli(1/2), X = X1 + X2 ~ Binomial(2, 1/2)
import numpy as np
import matplotlib.pyplot as plt
from math import comb

k = np.arange(3)
pX = np.array([comb(2, j) for j in k]) / 4               # p_X(k) = 2Ck / 4
pX_young = np.array([0, 0.5, 0.5])                        # X = X1 + 1 given X2 = 1
pX_atleast = np.where(k >= 1, pX, 0) / pX[1:].sum()       # p_X(k)/(1 - p_X(0)), k >= 1
print("Theory: P(X=2 | X2=1) =", pX_young[2], ", P(X=2 | X>=1) =", pX_atleast[2])

rng = np.random.default_rng(0)
N = 1_000_000
X1 = rng.integers(0, 2, N)          # 1 = girl
X2 = rng.integers(0, 2, N)
X = X1 + X2
sim_pX = np.bincount(X, minlength=3) / N
sim_young = np.bincount(X[X2 == 1], minlength=3) / np.sum(X2 == 1)
sim_atleast = np.bincount(X[X >= 1], minlength=3) / np.sum(X >= 1)
print("Simulation: P(X=2 | X2=1) =", sim_young[2], ", P(X=2 | X>=1) =", sim_atleast[2])
print("p_X theory    :", pX, "\np_X simulation:", sim_pX)

fig, ax = plt.subplots(1, 3, figsize=(13, 4))
for a, th, sm, title in ((ax[0], pX, sim_pX, r'$p_X(k)$'),
                         (ax[1], pX_young, sim_young, r'$p_{X|X_2}(k|1)$'),
                         (ax[2], pX_atleast, sim_atleast, r'$p_{X|X\geq 1}(k)$')):
    a.stem(k - 0.05, th, linefmt='b-', markerfmt='bo', basefmt=' ', label='Theory')
    a.stem(k + 0.05, sm, linefmt='r--', markerfmt='rs', basefmt=' ', label='Simulation')
    a.set_title(title)
    a.set_xlabel('$k$ (number of girls)')
    a.set_xticks(k)
    a.set_ylim(0, 0.8)
    a.grid(True, linestyle='--', alpha=0.5)
    a.legend()
plt.tight_layout()
plt.savefig('figs/1.2.12.png')
