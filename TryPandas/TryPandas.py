import pandas as pd
import numpy as np

# data = np.array(['a', 'b', 'c', 'd'])
#
# s = pd.Series(data=data, index=[100, 101, 102, 103])
#
# print(s)

data = {'a': 1, 'b': 2, 'c': 3}

s = pd.Series(data=data, index=['b', 'c', 'd', 'a'])

# print(s)
# print(s[0])
# print(s[:2])
# print(s[2:])
# print(s[-2])
print(s['f'])
