import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import pytz
from pytz import timezone


def create_constants():
    print 'Creating constants...'
    constants = {
        # 'stock_filename': 'stock-prices/AAPL-day.csv'
        'stock_filename': 'stock-prices/AAPL-60min.csv'
        # 'stock_filename': 'stock-prices/AAPL-30min.csv'
    }

    return constants

def create_dataframe(stock_filename, has_time):
    print 'Creating dataframe with stock_filename ', stock_filename, 'and has_time ', has_time
    if has_time == True:
        columns = ['date', 'time', 'open', 'high', 'low', 'close', 'volume']
        df = pd.read_csv(stock_filename, names=columns)
        df = pd.DataFrame({
            'date': df['date'],
            'time': df['time'],
            'close': df['close']
        })

    else:
        columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        df = pd.read_csv(stock_filename, names=columns)
        df = pd.DataFrame({
            'close': df['close'],
            'date': df['date']
        })

    return df

# Creates a moving average of 8 items (hours or half an hours) so the intraday ups and downs are less drastic

def create_moving_average(df):
    print 'Creating moving averages'
    df['close 8ma'] = df['close'].rolling(window=8, min_periods=0).mean()

def add_change_column(df):
    print 'Adding change column'
    for i, row in df.iterrows():
        if i < (len(df) - 1):
            close = df.loc[i, 'close 8ma']
            close_next = df.loc[i + 1, 'close 8ma']
            close_change = (close_next - close)/close*100
            df.loc[i, 'change'] = close_change
            print df.loc[i]

    df.dropna(inplace=True)
    print df

def change_date_to_utc(df):
    print 'Changing datetime to UTC'
    for i, row in df.iterrows():
        date = df.loc[i, 'date'].split('/')
        time = df.loc[i , 'time'].split(':')

        year = int(date[2])
        month = int(date[0])
        day = int(date[1])
        hour = int(time[0])
        minute = int(time[1])

        ny_timezone = timezone('America/New_York')
        eastern = timezone('US/Eastern')
        utc = datetime(year, month, day, hour, minute, 0, 0, tzinfo=pytz.FixedOffset(-300))

        df.loc[i, 'utc'] = str(utc)
        print utc

def plot_stock(df):
    print 'Creating the plot'
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

    ax1.plot(df.index, df['close'])
    ax1.plot(df.index, df['close 8ma'])

    plt.show()

def save_df_to_csv(filename, df):
    print 'Saving CSV...'
    df.to_csv(filename)

def init():
    constants = create_constants()
    df = create_dataframe(constants['stock_filename'], True)
    create_moving_average(df)
    add_change_column(df)
    change_date_to_utc(df)
    print df.head()
    save_df_to_csv('AAPL-60min.csv', df)
    # plot_stock(df)

init()
