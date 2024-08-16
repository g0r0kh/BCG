import pandas as pd
import numpy as np

# import xlsx
data = pd.read_excel('source/agency_market_data_.xlsx',
                     sheet_name='sheet1')


# Combine columns into a new column 'Combined'
data['period'] = data['year'].astype(str) + data['quart'].astype(str)
data['color'] = np.where(data.Метка == 'ATX', 'g', 'b')

# cut base period
data_cut = data[data['year'] != 19]






