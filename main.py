from Traders import emptyTrader
from Traders import randomTrader
from Traders import solidTrader
from traderHandler import TraderHandler
from stockHandler import run_stock_exchange

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
    run_stock_exchange(trader_handler, INIT_STOCK, COMMISSION, LAST_DAY)
    
    print()
    print("*** Stock exchange simulation ended ***")
    print()
    trader_handler.pretty_print()

if __name__ == "__main__":
    main()