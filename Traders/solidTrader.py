from Traders import traderBot

"""
This trader treats the stock as long time investment,
buying only on the first 3 days and selling all on the last day.
"""
class SolidTrader(traderBot.TraderBot):
    _name = "netzer_solid"
    
    def buy_offer(self, money: int, value: int, price: int, metadata) -> bool:
        return metadata["current_day"] in [1, 2, 3]
    
    def sell_stocks(self, money: int, stocks: int, value: int, metadata) -> int:
        return stocks if metadata["current_day"] == metadata["last_day"]  else 0