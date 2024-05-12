from Traders import traderBot

class EmptyTrader(traderBot.TraderBot):
    _name = "netzer_empty"
    
    def buy_offer(self, money: int, value: int, price: int, time) -> bool:
        # Empty trader does not buy
        return False    
    
    def sell_stocks(self, money: int, stocks: int, value: int, time) -> int:
        # Empty trader does not have stocks to sell
        return 0