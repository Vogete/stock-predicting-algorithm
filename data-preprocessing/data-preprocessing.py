import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv('stock-prices/AAPL-60min.csv', names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'])
dataframe = pd.DataFrame({
    'date-time': dataframe['date'] + '-' + dataframe['time'],
    'close': dataframe['close'],
    'volume': dataframe['volume']
})

dataframe.set_index('date-time', inplace=True)
print dataframe.head()

dataframe['close'].plot()
plt.show()
