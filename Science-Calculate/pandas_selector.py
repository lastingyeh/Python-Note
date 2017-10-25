import pandas as pd
import numpy as np
from util import s_print as p

dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
print('==============================')
print(df['A'])
print('==============================')
print(df.A)
print('==============================')
print(df.A)
print('==============================')
print(df[0:3])
print('==============================')
print(df['20130102':'20130104'])

# select by label:loc
print('==============================')
print(df.loc['20130102'])
print('==============================')
print(df.loc[:, ['A', 'B']])
print('==============================')
print(df.loc['20130102', ['A', 'B']])

# select by position: iloc r:(3-),c:0
p(df.iloc[3:, 0], 'iloc[3:,1]')
p(df.iloc[3:5, 1:3], 'df.iloc[3:5, 1:3]')

# mixed selection ix
p(df.ix[:3, ['A', 'C']])

# Boolean indexing
p(df[df.A > 8], 'df[df.A > 8]')
