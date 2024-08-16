
import time
import numpy as np
import matplotlib.pyplot as plt
from bcg import data, data_cut

sort_list = sorted(set(data_cut['period']))


plt.ion()
for i in sort_list:
    a = data[data['period'] == i]

    plt.clf()
    plt.grid()

    # figure name
    plt.suptitle('BCG, Pharmacy market, ATC vs ICD - 10, Ipsos: 2019-2022')
    # axes name axes limits
    plt.gca().set(xlim=(0.0, a.x.quantile(0.95)), ylim=(a.y.quantile(0.05), a.y.quantile(0.75)),
                  xlabel='market share, %', ylabel='evolution, %')


    # data point params
    scatter = plt.scatter(a.x, a.y, s=a.x * 10, c=a.color, alpha=0.5)

    # legend is disable cause one dimension

    # # labels
    a = a.reset_index()
    for ii in range(len(a.x)):
        if a.name_short[ii] != 'empty':
            plt.annotate(a.Метка[ii] + ':' + a.name_short[ii], (a.x[ii], a.y[ii]))
        else:
            continue


    # plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.99)


plt.ioff()


plt.show()



