import pandas as pd
import numpy as np
from util import s_print as p

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

p(df1, 'df1')
p(df2, 'df2')
p(df3, 'df3')

# ignore_index=True > index 重新編號
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)

p(res, 'res')

# join,['inner','outer']

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

p(df1, 'df1')
p(df2, 'df2')
# as outer-join -> fill NaN
res = pd.concat([df1, df2])

p(res, 'res by outer join')

res = pd.concat([df1, df2], join='inner', ignore_index=True)

p(res, 'res by inner join')

# join_axes
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])

p(res, 'res by (axis=1,join_axes=[df1.index])')

# append
res = df1.append([df2, df3], ignore_index=True)

p(res, 'append df2 with df1')

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res = df1.append(s1, ignore_index=True)

p(res, 'append one row')
