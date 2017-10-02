import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports', sep=',')
ufo['Location'] = ufo.City + ", " + ufo.State
print(ufo.head())
