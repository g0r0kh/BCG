import pandas as pd
import numpy as np

# import xlsx
data = pd.read_excel('source/agency_market_data_.xlsx',
                     sheet_name='sheet1')


# Combine columns into a new column 'Combined'
data['period'] = data['year'].astype(str) + data['quart'].astype(str)
data['color'] = np.where(data.Метка == 'ATX', 'g', 'b')
# iterable sorted list
# df['d'] = np.where(df.c > df.b, 'Type a', 'Type b')
# sort_list = sorted(set(data['period']))

# split fot graph combine
# ATX = data[data['Метка']  == 'ATX']  # flt
# MKB = data[data['Метка']  != 'ATX']  # flt






