import time
import numpy as np
import matplotlib.pyplot as plt
from bcg import data

# fig = plt.figure(figsize=(10, 10))
# ax = fig.add_subplot()

# figure name
# fig.suptitle('BCG, Pharmacy market, ATX vs MKB, Ipsos: 2019-2022')

sort_list = sorted(set(data['period']))

plt.ion()
for i in sort_list:
    a = data[data['period'] == i]
    # fig = plt.figure(figsize=(10, 10))
    plt.clf()
    # fig = plt.figure(figsize=(10, 10))
    # ax = fig.add_subplot()
    # axes name
    #     plt.gca().set(xlim=(0.0, data.x.quantile(0.95)), ylim=(data.y.quantile(0.05), data.y.quantile(0.95)),
    #                   xlabel='market share, %', ylabel='evolution, %')

    plt.gca().set(xlim=(0.0, 30.0), ylim=(-30, 30),
                  xlabel='market share, %', ylabel='evolution, %')

    plt.scatter(a.x, a.y, s=a.x * 5, c=a.color, alpha=0.5)
    # plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.27)

# legend
# ax.legend(sorted(set(data.Метка)))

# label
#     for ii in range(len(data.x)):
#         if data.name_short[ii] != 'empty':
#             ax.annotate(data.name_short[ii], (data.x[ii], data.y[ii]))
#         else:
#             continue
plt.ioff()

# ax.grid()
plt.show()
