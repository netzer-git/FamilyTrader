from traderBot import TraderBot

class EmptyTrader(TraderBot):
    _name = "empty"
    
    def buy_offer(self, money: int, value: int, price: int, time) -> bool:
        return False    
    
    def sell_stocks(self, money: int, stocks: int, value: int, time) -> int:
        return 0