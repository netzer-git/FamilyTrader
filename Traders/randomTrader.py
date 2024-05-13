from Traders import traderBot
import random as rnd

""" 
This trader buys and sells randomly,
It flips coin every time to decide if to buy or sell.
"""
class RandomTrader(traderBot.TraderBot):
    _name = "netzer_random"
    
    def buy_offer(self, money: int, value: int, price: int, metadata) -> bool:
        # flip a coin to decide
        return rnd.choice([True, False])
    
    def sell_stocks(self, money: int, stocks: int, value: int, metadata) -> int:
        # sell a coin to decide or on last day sell all
        if metadata["current_day"] == metadata["last_day"]:
            return stocks
        elif (rnd.choice([True, False]) and stocks > 0):
            # if True, random stocks to sell
            return rnd.randint(1, stocks)
        else:
            return 0