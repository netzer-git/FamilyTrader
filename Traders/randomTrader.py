from Traders import traderBot

class RandomTrader(traderBot.TraderBot):
    _name = None
    
    def buy_offer(self, money: int, value: int, price: int, time) -> bool:
        raise ValueError("sell_stocks should override")
    
    def buy_offer(self, money: int, value: int, price: int, time) -> bool:
        raise ValueError("sell_stocks should override")