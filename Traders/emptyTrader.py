from Traders import traderBot

""" 
This trader does not buy or sell. It is doing nothing and ends with the same money as it started.
Empty trader can be easily used as a template for new traders.
Change the name and implement the buy_offer and sell_stocks methods fully.
"""
class EmptyTrader(traderBot.TraderBot):
    _name = "netzer_empty"
    
    def buy_offer(self, money: int, value: int, price: int, metadata) -> bool:
        # Empty trader does not buy
        return False    
    
    def sell_stocks(self, money: int, stocks: int, value: int, metadata) -> int:
        # Empty trader does not have stocks to sell
        return 0