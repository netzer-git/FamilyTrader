
class TraderBot:
    _name = None
    
    def buy_offer(self, money: int, value: int, price: int, metadata) -> bool:
        raise ValueError("sell_stocks should override")
    
    def sell_stocks(self, money: int, stocks: int, value: int, metadata) -> int:
        raise ValueError("sell_stocks should override")
    
    def get_name(self) -> str:
        if self._name is None:
            raise ValueError("TraderBot should not be used directly")
        return self._name