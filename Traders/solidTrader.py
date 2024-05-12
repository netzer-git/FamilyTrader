from Traders import traderBot

class SolidTrader(traderBot.TraderBot):
    _name = "netzer_solid"
    
    def buy_offer(self, money: int, value: int, price: int, time) -> bool:
        return time[0] in [1, 2, 3]
    
    def sell_stocks(self, money: int, stocks: int, value: int, time) -> int:
        return stocks if time[0] == time[1] else 0