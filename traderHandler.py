from typing import List
from Traders import traderBot

class TraderHandler:
    def __init__(self, traders_input: List[traderBot.TraderBot], initial_money: int):
        self.traders = []
        for trader in traders_input:
            self.traders.append({
                "trader": trader,
                "money": initial_money,
                "stocks": 0
            })

    def activate_buy_phase(self, value: int, offers_per_trader: int, deviation: float, commission:int, time) -> int:
        # TODO
        pass

    def activate_sell_phase(self, value: int, commission: int, time ) -> int:
        total_sales = 0
        
        for traderInfo in self.traders:
            trader: traderBot.TraderBot = traderInfo["trader"]
            stocks_amount_to_sell = trader.sell_stocks(traderInfo["money"], traderInfo["stocks"], value, time)
            # apply sell effects
            if (0 < stocks_amount_to_sell <= traderInfo["stocks"]):
                traderInfo["money"] += stocks_amount_to_sell * value - stocks_amount_to_sell * commission
                traderInfo["stocks"] -= stocks_amount_to_sell
                total_sales += stocks_amount_to_sell
            
        return total_sales
    
    def pretty_print(self):
        for traderInfo in self.traders:
            trader: traderBot.TraderBot = traderInfo["trader"]
            print(f"{trader.get_name()} has {traderInfo['money']}$ and {traderInfo['stocks']} stocks")