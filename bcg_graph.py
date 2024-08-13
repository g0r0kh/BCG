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
ax.legend(sorted(set(data.Метка)))

# label atx

text_atx = ATX.name_short

for i in range(len(ATX.x)):
    ax.annotate(text_atx[i], (x_atx[i], y_atx[i]))

# label mkb

# text_mkb = MKB.name_short
# #
# for ii in range(len(MKB.x)):
#     ax.annotate(text_mkb[ii], (x_mkb[ii], y_mkb[ii]))




ax.grid()
plt.show()