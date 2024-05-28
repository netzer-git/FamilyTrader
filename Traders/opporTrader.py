from Traders import traderBot

class opporTrader(traderBot.TraderBot):
    _name = "netzer_opportunist"
    
    def buy_offer(self, money: int, value: int, price: int, metadata) -> bool:
        days_to_buy = [1, 2] + [metadata["last_day"] - 2, metadata["last_day"] - 1]
        return metadata["current_day"] in days_to_buy
    
    def sell_stocks(self, money: int, stocks: int, value: int, metadata) -> int:
        days_to_sell = [3] + [metadata["last_day"] - 1]
        return stocks if metadata["current_day"] in days_to_sell else 0