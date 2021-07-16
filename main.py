import pandas as pd
import numpy as np
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema as ae

search_term = 'Apple Stock'
n = 20

pytrend = TrendReq()

pytrend.build_payload(kw_list=[search_term])

df = pytrend.interest_over_time()
y = df[search_term].values.tolist() # .values.tolist())
x = list(df.index)

# print(df.to_string())
# print(x)
# print(y)

df['min'] = df.iloc[ae(df[search_term].values, np.less_equal, order=n)[0]][search_term]
df['max'] = df.iloc[ae(df[search_term].values, np.greater_equal, order=n)[0]][search_term]

plt.plot(x, y)
plt.scatter(df.index, df['min'], c='r')
plt.scatter(df.index, df['max'], c='g')

loc_min = []
loc_max = []
for date in df.index:
    if not df['min'].isnull()[date]:
        loc_min.append((date, df['min'][date]))
    elif not df['max'].isnull()[date]:
        loc_max.append((date, df['max'][date]))

print('loc min')
for i in loc_min:
    print(i)
print('loc max')
for i in loc_max:
    print(i)

plt.show()
