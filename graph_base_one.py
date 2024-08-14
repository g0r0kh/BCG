import numpy as np
import matplotlib.pyplot as plt
from bcg import data

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()

# figure name
fig.suptitle('BCG, Pharmacy market, ATX vs MKB, Ipsos: 2019-2022')

# axes name
plt.gca().set(xlim=(0.0, data.x.quantile(0.95)), ylim=(data.y.quantile(0.05), data.y.quantile(0.95)),
              xlabel='market share, %', ylabel='evolution, %')

# plt.gca().set(xlim=(0.0, 30.0), ylim=(-30, 30),
#               xlabel='market share, %', ylabel='evolution, %')

ax.scatter(data.x, data.y, s=data.x*5, c=data.color, alpha=0.5)

# legend
# ax.legend(sorted(set(data.Метка)))

# label

for i in range(len(data.x)):
    if data.name_short[i] != 'empty':
        ax.annotate(data.name_short[i], (data.x[i], data.y[i]))
    else:
        continue

ax.grid()
plt.show()