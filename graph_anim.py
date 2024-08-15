import time
import numpy as np
import matplotlib.pyplot as plt
from bcg import data

sort_list = sorted(set(data['period']))


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
    # legend
    # plt.legend(handles=scatter.legend_elements()[0], labels=classes)

    # plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.19)



# # label
# for ii in range(len(data.x)):
#     if data.name_short[ii] != 'empty':
#         plt.annotate(data.name_short[ii], (data.x[ii], data.y[ii]))
#     else:
#         continue
# # label sample
# legend=[str(year) for year in df['year'].unique()]
# plt.title('Battery Capicity kwh')
# result = plt.scatter('Approx_Release_price_order_in_K$','Battery_Capacity_kWh',data=df,c='year',label='Class 1')
# plt.ylabel('kwh')
# plt.xlabel('K$')
# plt.legend(handles=result.legend_elements()[0],
#        labels=legend,
#        title="Year")
# print('The higher priced evs have more battery capacity')


plt.ioff()


plt.show()



