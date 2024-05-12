from traderHandler import TraderHandler
import random as rnd

def run_stock_exchange(trader_handler: TraderHandler, init_stock: int, commission: int, last_day: int):
    current_day = 1
    deviation = 0.1
    offers_per_trader = 2
    current_stock_value = init_stock
    stocks_in_market = 0
    
    while current_day <= last_day:
        # buy phase
        day_buys = trader_handler.activate_buy_phase(current_stock_value, offers_per_trader, deviation, commission, [current_day, last_day])
        # sell phase
        day_sells = trader_handler.activate_sell_phase(current_stock_value, commission, [current_day, last_day])
        # adjust stock phase
        stocks_in_market += day_buys - day_sells
        current_stock_value = adjust_stock_value(current_stock_value, day_buys, day_sells, deviation, stocks_in_market)
        # day advance
        print(f"Day {current_day} ended. Stock value: {current_stock_value}. Stocks in market: {stocks_in_market}")
        print()
        current_day += 1

def adjust_stock_value(value: int, day_buys: int, day_sells: int, deviation: float, stocks_in_market: int) -> int:
    # raise the value in % by the difference between buys and sells
    if stocks_in_market == 0:
        stocks_in_market = 1

    impact = (day_buys - day_sells) * (value * 0.1) * (1 / stocks_in_market)
    # add a random deviation
    chip = rnd.randint(-int(value * deviation), int(value * deviation))
    return value + chip + impact