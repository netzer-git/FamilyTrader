from Traders import emptyTrader
from Traders import randomTrader
from Traders import solidTrader
from Traders import traderBot
from Traders import impulseTrader
from Traders import opporTrader
from traderHandler import TraderHandler
from stockHandler import run_stock_exchange

import time
import config
import matplotlib.pyplot as plt

INIT_MONEY = 1_000
INIT_STOCK = 100
COMMISSION = 1
LAST_DAY = 10

traders = [
    emptyTrader.EmptyTrader(),
    randomTrader.RandomTrader(),
    solidTrader.SolidTrader(),
    impulseTrader.ImpulseTrader(),
    opporTrader.opporTrader()
]

def stock_exchange_wrapper(traders, debug=False):
    config.config_properties.DEBUG = debug
    
    if config.config_properties.DEBUG:
        print()
        print("*** Stock exchange simulation started ***")
        print()
        time.sleep(config.config_properties.big_sleep)
    
    trader_handler = TraderHandler(traders, INIT_MONEY)
    metadata = run_stock_exchange(trader_handler, INIT_STOCK, COMMISSION, LAST_DAY)

    if config.config_properties.DEBUG:
        print()
        print("*** Stock exchange simulation ended ***")
        print()
        time.sleep(config.config_properties.big_sleep)
    
    trader_handler.pretty_print()

    return metadata

def main():
    metadata = stock_exchange_wrapper(traders=traders, debug=True)

    # paint stocks plots
    fig, ax = plt.subplots()
    ax.plot(range(1, 11), metadata["stocks_data"],)
    ax.set(xlabel='Day', ylabel='Price',
        title='Stock prices over the week')
    ax.grid()
    plt.show()

if __name__ == "__main__":
    main()