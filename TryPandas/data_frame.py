import pandas as pd

# data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
#
# df = pd.DataFrame(data=data, columns=['Name', 'Age'], dtype=float)

data = {
    'Name': ['Alex', 'Bob', 'Clarke'],
    'Age': [10, 12, 13]
}

df = pd.DataFrame(data=data)
print(df[1:2])