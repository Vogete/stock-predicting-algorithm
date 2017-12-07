from zipline.api import order, record, symbol, history
from zipline import run_algorithm
from datetime import datetime
import pytz

def initialize(context):
    context.assets = symbol('AAPL')
    pass

def handle_data(context, data):
    adat = data.history(
        context.assets,
        fields='price',
        bar_count=1,
        frequency='1d'
    )

    print "AAPL:"
    print adat


start = "2015-01-01"
end = "2015-02-01"
# start = datetime(2015, 1, 1)
# end = datetime(2015, 12, 31)

run_algorithm(start, end, initialize, 1000000, handle_data)
