import numpy as np

rng = np.random.default_rng(0)
N = 1_000_000

# 1 = girl, 0 = boy; column 0 = elder child, column 1 = younger child
kids = rng.integers(0, 2, size=(N, 2))
both = (kids[:, 0] == 1) & (kids[:, 1] == 1)
youngest_girl = kids[:, 1] == 1
atleast_one_girl = (kids[:, 0] == 1) | (kids[:, 1] == 1)

print("P(both girls | youngest is a girl)  =", both[youngest_girl].mean())
print("P(both girls | at least one a girl) =", both[atleast_one_girl].mean())
