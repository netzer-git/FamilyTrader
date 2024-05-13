from traderHandler import TraderHandler
import random as rnd
import config
import time

def run_stock_exchange(trader_handler: TraderHandler, init_stock: int, commission: int, last_day: int):
    current_day = 1
    deviation = 0.1
    offers_per_trader = 2
    current_stock_value = init_stock
    stocks_in_market = 0
    
    # review data objects
    stocks_data = []
    
    # running day loop
    while current_day <= last_day:
        metadata = { "current_day": current_day, "last_day": last_day}
        # buy phase
        day_buys = trader_handler.activate_buy_phase(current_stock_value, offers_per_trader, deviation, commission, metadata)
        # sell phase
        day_sells = trader_handler.activate_sell_phase(current_stock_value, commission, metadata)
        # adjust stock phase
        stocks_in_market += day_buys - day_sells
        stocks_data.append(current_stock_value)
        current_stock_value = adjust_stock_value(current_stock_value, day_buys, day_sells, deviation, stocks_in_market)
        # advance day
        if config.config_properties.DEBUG:
            print(f"Day {current_day} ended. Stock value: {current_stock_value}. Stocks in market: {stocks_in_market}")
            print()
            time.sleep(config.config_properties.big_sleep)

        current_day += 1
        
    return { "stocks_data": stocks_data }

def adjust_stock_value(value: int, day_buys: int, day_sells: int, deviation: float, stocks_in_market: int) -> int:
    # raise the value in % by the difference between buys and sells
    if stocks_in_market == 0:
        stocks_in_market = 1

    impact = int((day_buys - day_sells) * (value * 0.1) * (1 / stocks_in_market))
    # add a random deviation
    chip = rnd.randint(-int(value * deviation), int(value * deviation))
    # TODO add the natural grow impact - the market always wins
    return max(value + chip + impact, 1)