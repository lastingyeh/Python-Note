import pandas as pd
import numpy as np
from util import s_print as p

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan

p(df, 'Original df')

# as how='all' must be axis 'all nan'
p(df.dropna(axis=0, how='all', ), 'dropna')  # how={'any','all'}

p(df.isnull(), 'df.isnull() -> return []')

p(np.any(df.isnull()), 'np.any(df.isnull()) -> Bool')

p(df.fillna(value=0), 'df.fillna(value=0) => nan > 0')
