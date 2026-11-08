import numpy as np

# cot^{-1}[(sqrt(1+sin x)+sqrt(1-sin x))/(sqrt(1+sin x)-sqrt(1-sin x))] = x/2
x = np.linspace(0.01, np.pi / 4 - 0.01, 8)
num = np.sqrt(1 + np.sin(x)) + np.sqrt(1 - np.sin(x))
den = np.sqrt(1 + np.sin(x)) - np.sqrt(1 - np.sin(x))
lhs = np.pi / 2 - np.arctan(num / den)      # cot^{-1}(t) = pi/2 - tan^{-1}(t), t > 0
rhs = x / 2
print(np.column_stack((x, lhs, rhs)))
print("Max error:", np.max(np.abs(lhs - rhs)))
