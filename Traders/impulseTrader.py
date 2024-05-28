from Traders import traderBot

class ImpulseTrader(traderBot.TraderBot):
    _name = "netzer_impulsive"
    
    _stocks_bought_price = dict()
    
    def buy_offer(self, money: int, value: int, price: int, metadata) -> bool:
        # buy if the price is lower than the value
        if price < value:
            if price in self._stocks_bought_price:
                self._stocks_bought_price[price] += 1
            else:
                self._stocks_bought_price[price] = 1
            
            return True
        
        return False
    
    def sell_stocks(self, money: int, stocks: int, value: int, metadata) -> int:
        if metadata["current_day"] == metadata["last_day"]:
            return stocks
        
        amount_to_sell = 0
        for price in self._stocks_bought_price:
            if price > value:
                amount_to_sell += self._stocks_bought_price[price]
                self._stocks_bought_price[price] = 0
        
        return amount_to_sell