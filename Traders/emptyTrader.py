from Traders import traderBot

""" 
This trader does not buy or sell. It is doing nothing and ends with the same money as it started.
"""
class EmptyTrader(traderBot.TraderBot):
    _name = "netzer_empty"
    
    def buy_offer(self, money: int, value: int, price: int, time) -> bool:
        # Empty trader does not buy
        return False    
    
    def sell_stocks(self, money: int, stocks: int, value: int, time) -> int:
        # Empty trader does not have stocks to sell
        return 0