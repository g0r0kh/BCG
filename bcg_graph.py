import numpy as np
import matplotlib.pyplot as plt
from bcg import ATX, MKB, data

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()

# figure name
fig.suptitle('BCG, Pharmacy market, ATX vs MKB, Ipsos: 2019-2022')

# axes name
plt.gca().set(xlim=(0.0, 30.0), ylim=(-30, 30),
              xlabel='market share, %', ylabel='evolution, %')

# values
x_atx = ATX.x
y_atx = ATX.y

x_mkb = MKB.x
y_mkb = MKB.y

ax.scatter(x_atx, y_atx, 200, alpha=0.5)
ax.scatter(x_mkb, y_mkb, 200, alpha=0.5)

# legend
ax.legend(set(data.Метка))





ax.grid()
plt.show()