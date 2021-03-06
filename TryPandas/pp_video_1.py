import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import datetime

style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 1, 1)

df = web.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()

plt.show()
