import time
import matplotlib.pyplot as plt
from bcg import data_cut

sort_list = sorted(set(data_cut['period']))

plt.ion()

plt.figure(figsize=(9, 9))

for i in sort_list:
    a = data_cut[data_cut['period'] == i]
    a = a.reset_index()
    plt.clf()
    plt.grid()

    # figure name
    plt.suptitle(f'BCG, Pharmacy market, ATC vs ICD - 10, Ipsos: {a.quart[0]} quart {a.year[0]} year')
    plt.title('Матрица БКГ, Категория(Нозология МКБ 10 ) + Субкатегория(Классификация АТХ), \n'
              'источник Ipsos, Пациентопоток — Назначения препарата, 2019-2022 кв.')
    # axes name axes limits
    plt.gca().set(xlim=(0.0, a.x.quantile(0.95)), ylim=(a.y.quantile(0.05), a.y.quantile(0.75)),
                  xlabel='market share, %\nдоля рынка, %', ylabel='evolution, %\nизменение, %')

    # data point params
    scatter = plt.scatter(a.x, a.y, s=a.x * 21, c=a.color, alpha=0.5)

    # legend is disable cause one dimension

    # # labels

    for ii in range(len(a.x)):
        if a.name_short[ii] != 'empty':
            plt.annotate(a.Метка[ii] + ':\n ' + a.name_short[ii], (a.x[ii], a.y[ii]))
        else:
            continue

    # plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.99)

plt.ioff()

plt.show()
