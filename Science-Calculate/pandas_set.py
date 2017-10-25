import pandas as pd
import numpy as np
from util import s_print as p

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

p(df, 'Original df')

# df.iloc[2, 2] = 1111
#
# p(df, 'Modified df by iloc')
#
# df.loc['20130101', 'B'] = 2222
#
# p(df, 'Modified df by loc')
#
# df[df.A > 4] = 0
#
# p(df, 'df[df.A > 4] = 0')

# 僅 column A value > 4 set 0
# df.A[df.A > 4] = 0
# p(df, 'df.A[df.A > 4] = 0')

# As column A value > 4 set column B value 0
# df.B[df.A > 4] = 0
# p(df, 'df.B[df.A > 4] = 0')

df['F'] = np.nan

p(df, 'add F column')

df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130101', periods=6))

p(df, 'add E column, set new series')
