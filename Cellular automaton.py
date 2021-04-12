import numpy as np
import matplotlib.pyplot as plt

n = 18  # правило
s = 300  # ширина
d = 110  # длина
rule = np.array(list(map(int, np.binary_repr(n, 8))))[::-1]

f = np.zeros((d, s), dtype=int)

f[0, s // 2] += 1

for i in range(1, d):
    idx = 4 * np.roll(f[i - 1], 1) + 2 * f[i - 1] + np.roll(f[i - 1], -1)
    f[i] = rule[idx]

fig, ax = plt.subplots()

ax.imshow(f, cmap='GnBu')

fig.set_figwidth(13)
fig.set_figheight(13)

plt.show()