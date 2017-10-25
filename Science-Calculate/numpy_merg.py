import pandas as pd
import numpy as np
from util import s_print as p

left = pd.DataFrame({
	'key': ['K0', 'K1', 'K2', 'K3'],
	'A': ['A0', 'A1', 'A2', 'A3'],
	'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
	'key': ['K0', 'K1', 'K2', 'K3'],
	'C': ['C0', 'C1', 'C2', 'C3'],
	'D': ['D0', 'D1', 'D2', 'D3']
})

p(left, 'left')
p(right, 'right')

# merge
res = pd.merge(left, right, on='key')

p(res, 'res merge')

# consider two keys

left = pd.DataFrame({
	'key1': ['K0', 'K0', 'K1', 'K2'],
	'key2': ['K0', 'K1', 'K0', 'K1'],
	'A': ['A0', 'A1', 'A2', 'A3'],
	'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
	'key1': ['K0', 'K1', 'K1', 'K2'],
	'key2': ['K0', 'K0', 'K0', 'K0'],
	'C': ['C0', 'C1', 'C2', 'C3'],
	'D': ['D0', 'D1', 'D2', 'D3']
})

p(left, 'left')
p(right, 'right')

# how = ['left','right','outer','inner']
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')

p(res, 'res merge by two keys (inner)')

res = pd.merge(left, right, on=['key1', 'key2'], how='outer')

p(res, 'res merge by two keys (outer)')

res = pd.merge(left, right, on=['key1', 'key2'], how='right')

p(res, 'res merge by two keys (right)')

res = pd.merge(left, right, on=['key1', 'key2'], how='left')

p(res, 'res merge by two keys (left)')

# indicator
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})

p(df1, 'df1')
p(df2, 'df2')

# show c[_merge] as if it has data
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')

p(res, 'res by indicator')

# index
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
										'B': ['B0', 'B1', 'B2']},
									 index=['K0', 'K1', 'K2'])

df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
										'D': ['D0', 'D1', 'D2']},
									 index=['K0', 'K2', 'K3'])

p(df1, 'df1')
p(df2, 'df2')

res = pd.merge(df1, df2, left_index=True, right_index=True, how='outer')

p(res, 'res left & right index')

# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

p(boys, 'boys')
p(girls, 'girls')

# fill colsName _boy & _girl
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='outer')

p(res, 'res suffixes')
