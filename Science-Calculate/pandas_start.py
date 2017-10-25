import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])

print('s = \n', s)

dates = pd.date_range('20160101', periods=6)

print('dates = ', dates)

# 隨機產生 r6,c4 數值 設定 row-index value = dates(6), columns-index = ['a','b','c','d'] (4)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])

print('df = ', df)

# default rows(0,1,2) & columns(0,1,2,3)
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))

print('df1 = ', df1)

df2 = pd.DataFrame({'A': 1.,
										'B': pd.Timestamp('20130102'),
										'C': pd.Series(1, index=list(range(4)), dtype='float32'),
										'D': np.array([3] * 4, dtype='int32'),
										'E': pd.Categorical(['test', 'train', 'test', 'train']),
										'F': 'foo'})

print('df2 = \n', df2)
print('df2.dtypes =\n', df2.dtypes)
print('df2.index:\n', df2.index)
print('df2.columns\n', df2.columns)
print('df2.values\n', df2.values)
# 忽略無法計算部分
print('df2.describe()', df2.describe())
# 轉置矩陣
print('df2.T\n', df2.T)

df3 = df2.sort_index(axis=1, ascending=False)

print('sort by axis=1 \n', df3)

df4 = df2.sort_index(axis=0, ascending=False)

print('sort by axis=0 \n', df4)

# 特定行排序
df5 = df2.sort_values(by='E')

print('sort by E\n', df5)
