import matplotlib.pyplot as plt
import pandas as pd

# stock_filename = 'stock-prices/AAPL-60min.csv'
# columns ['date', 'time', 'open', 'high', 'low', 'close', 'volume']

stock_filename = 'stock-prices/AAPL-day.csv'
columns = ['date', 'open', 'high', 'low', 'close', 'volume']

df = pd.read_csv(stock_filename, names=columns)
df = pd.DataFrame({
    'close': df['close']
})

# df = pd.df({
#     'date-time': df['date'] + '-' + df['time'],
#     'close': df['close']
# })

# df.set_index('date-time', inplace=True)

# Creates a moving average of 8 items (hours or half an hours) so the intraday ups and downs are less drastic
df['close 8ma'] = df['close'].rolling(window=8, min_periods=0).mean()

for i, row in df.iterrows():
    if i < (len(df) - 1):
        close = df.loc[i, 'close 8ma']
        close_next = df.loc[i + 1, 'close 8ma']
        close_change = (close_next - close)/close*100

        df.loc[i, 'change'] = close_change

        print 'close: ', close
        print 'close_next: ', close_next
        print 'close_change', close_change

print df

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

ax1.plot(df.index, df['close'])
ax1.plot(df.index, df['close 8ma'])

plt.show()


