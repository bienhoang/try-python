import pandas as pd

bugs = pd.read_csv('bugs.csv', sep=',', names=['Sentence', 'Expected', 'Result'])

print(bugs['Result'].head(10))
