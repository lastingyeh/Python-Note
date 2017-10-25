import pandas as pd
import numpy as np
from util import s_print as p

data = pd.read_csv('student.csv')

p(data, 'Read student.csv')

data.to_pickle('student.pickle')

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
