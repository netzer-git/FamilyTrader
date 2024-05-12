from Traders import emptyTrader
from Traders import randomTrader
from Traders import solidTrader
from traderHandler import TraderHandler
from stockHandler import run_stock_exchange

import matplotlib.pyplot as plt

INIT_MONEY = 1_000
INIT_STOCK = 100
COMMISSION = 1
LAST_DAY = 10

traders = [
    emptyTrader.EmptyTrader(),
    emptyTrader.EmptyTrader(),
    randomTrader.RandomTrader(),
    randomTrader.RandomTrader(),
    solidTrader.SolidTrader(),
    solidTrader.SolidTrader(),
]

def main():
    trader_handler = TraderHandler(traders, INIT_MONEY)
    metadata = run_stock_exchange(trader_handler, INIT_STOCK, COMMISSION, LAST_DAY)
    
    print()
    print("*** Stock exchange simulation ended ***")
    print()
    trader_handler.pretty_print()

    # paint stocks plots
    fig, ax = plt.subplots()
    ax.plot(range(1, 11), metadata["stocks_data"],)
    ax.set(xlabel='Day', ylabel='Price',
        title='Stock prices over the week')
    ax.grid()
    plt.show()

if __name__ == "__main__":
    main()