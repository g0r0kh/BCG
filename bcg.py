import pandas as pd
import numpy as np

# import xlsx
data = pd.read_excel('source/agency_market_data.xlsx',
                     sheet_name='sheet1')
# split fot graph combine
ATX = data[data['Метка']  == 'ATX']  # flt
MKB = data[data['Метка']  != 'ATX']  # flt






# b.to_excel('result_ex1.xlsx',
#               sheet_name='sheet_nm',
#               index=True)

# #
# data['Terr']=np.where(data['Name'].str.endswith('Гинеколог'),
#                       data['Name'].str.split(' ', n=1).str[0],
#                       np.nan)
#
# data['Terr'] = data['Terr'].ffill()
#
# data = data[data['Name'].notnull()]
#
# data.to_excel('result_ex1.xlsx',
#               sheet_name='sheet_nm',
#               index=True)