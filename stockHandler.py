from traderHandler import TraderHandler


def run_stock_exchange(trader_handler: TraderHandler, init_stock: int, commission: int, last_day: int):
    current_day = 1
    deviation = 0.1
    offers_per_trader = 2
    current_stock_value = init_stock
    
    while current_day <= last_day:
        # buy phase
        day_buys = trader_handler.activate_buy_phase(current_stock_value, offers_per_trader, deviation, commission, [current_day, last_day])
        # sell phase
        day_sells = trader_handler.activate_sell_phase(current_stock_value, commission, [current_day, last_day])
        # adjust stock phase
        current_stock_value = adjust_stock_value(current_stock_value, day_buys, day_sells)
        # day advance
        print(f"Day {current_day} ended")
        current_day += 1
    
    print("Stock exchange simulation ended")
    trader_handler.pretty_print()

def adjust_stock_value(value: int, day_buys: int, day_sells: int) -> int:
    # TODO
    return value + 1