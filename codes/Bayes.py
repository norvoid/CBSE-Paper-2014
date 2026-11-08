import numpy as np
from math import comb
from fractions import Fraction

# Exact: E1 = lost card is a spade, E2 = it is not
P_E1, P_E2 = Fraction(1, 4), Fraction(3, 4)
P_A_E1 = Fraction(comb(12, 3), comb(51, 3))
P_A_E2 = Fraction(comb(13, 3), comb(51, 3))
post = P_A_E1 * P_E1 / (P_A_E1 * P_E1 + P_A_E2 * P_E2)
print("P(E1|A) =", post, "=", float(post))

# Monte Carlo: lose a card, then draw three from the remaining 51
rng = np.random.default_rng(0)
N = 400_000
deck = np.arange(52)              # cards 0..12 are spades
hits = total = 0
for _ in range(N):
    perm = rng.permutation(52)
    lost, draw = perm[0], perm[1:4]
    if np.all(draw < 13):
        total += 1
        hits += lost < 13
print("Simulated P(E1|A) =", hits / total)
