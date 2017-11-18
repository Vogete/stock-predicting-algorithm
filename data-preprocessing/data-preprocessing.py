import matplotlib.pyplot as plt
import pandas as pd

# stock_filename = 'stock-prices/AAPL-60min.csv'
stock_filename = 'stock-prices/AAPL-day.csv'

def create_dataframe(stock_filename, has_time):
    if has_time == True:
        columns = ['date', 'time', 'open', 'high', 'low', 'close', 'volume']
        df = pd.read_csv(stock_filename, names=columns)
        df = pd.DataFrame({
            'datetime': df['date'] + '-' + df['time'],
            'close': df['close']
        })

    else:
        columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        df = pd.read_csv(stock_filename, names=columns)
        df = pd.DataFrame({
            'close': df['close']
        })

    return df

df = create_dataframe(stock_filename, False)

# Creates a moving average of 8 items (hours or half an hours) so the intraday ups and downs are less drastic

df['close 8ma'] = df['close'].rolling(window=8, min_periods=0).mean()

def add_change_column():
    print len(df)
    for i, row in df.iterrows():
        if i < (len(df) - 1):
            close = df.loc[i, 'close 8ma']
            close_next = df.loc[i + 1, 'close 8ma']
            close_change = (close_next - close)/close*100

            df.loc[i, 'change'] = close_change

            print df.loc[i]

    df.dropna(inplace=True)

add_change_column()

print df

def plot_stock():
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

    ax1.plot(df.index, df['close'])
    ax1.plot(df.index, df['close 8ma'])

    plt.show()
