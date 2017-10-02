import pandas as pd

orders = pd.read_table('http://bit.ly/chiporders')

user_cols = ['no', 'user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)

print(users.head())

