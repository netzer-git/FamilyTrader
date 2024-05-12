from Traders import emptyTrader
from traderHandler import TraderHandler
from stockHandler import run_stock_exchange

INIT_MONEY = 1_000
INIT_STOCK = 100
COMMISSION = 1
LAST_DAY = 10

traders = [
    emptyTrader.EmptyTrader(),
    emptyTrader.EmptyTrader(),
    emptyTrader.EmptyTrader(),
]

def main():
    trader_handler = TraderHandler(traders, INIT_MONEY)
    run_stock_exchange(trader_handler, INIT_STOCK, COMMISSION, LAST_DAY)

if __name__ == "__main__":
    main()