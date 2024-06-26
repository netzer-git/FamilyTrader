from typing import List
from Traders import traderBot
import random as rnd
import config
import time

class TraderHandler:
    def __init__(self, traders_input: List[traderBot.TraderBot], initial_money: int):
        self.traders = []
        for trader in traders_input:
            self.traders.append({
                "trader": trader,
                "money": initial_money,
                "stocks": 0
            })

    def activate_buy_phase(self, value: int, offers_per_trader: int, deviation: float, commission: int, metadata) -> int:
        refused_offers = []
        today_buys = 0
        
        for i in range(offers_per_trader):
            for traderInfo in self.traders:
                trader: traderBot.TraderBot = traderInfo["trader"]
                offer_price = self.generate_stock_price(value, deviation)
                
                if trader.buy_offer(traderInfo["money"], value, offer_price, metadata):
                    traderInfo["money"] -= value + commission
                    traderInfo["stocks"] += 1
                    today_buys += 1

                    if config.config_properties.DEBUG:
                        print(f"{trader.get_name()} bought a stock at {offer_price}")
                        time.sleep(config.config_properties.medium_sleep)

                else:
                    refused_offers.append(offer_price)

                    if config.config_properties.DEBUG:
                        print(f"{trader.get_name()} refused a stock at {offer_price}")
                        time.sleep(config.config_properties.medium_sleep)
        
        return today_buys
        

    def activate_sell_phase(self, value: int, commission: int, metadata) -> int:
        total_sales = 0
        
        for traderInfo in self.traders:
            trader: traderBot.TraderBot = traderInfo["trader"]
            stocks_amount_to_sell = trader.sell_stocks(traderInfo["money"], traderInfo["stocks"], value, metadata)
            # apply sell effects
            if (0 < stocks_amount_to_sell <= traderInfo["stocks"]):
                traderInfo["money"] += stocks_amount_to_sell * value - stocks_amount_to_sell * commission
                traderInfo["stocks"] -= stocks_amount_to_sell
                total_sales += stocks_amount_to_sell

                if config.config_properties.DEBUG:
                    print(f"{trader.get_name()} sold {stocks_amount_to_sell} stocks")
                    time.sleep(config.config_properties.medium_sleep)
            
        return total_sales
    
    def pretty_print(self):
        for traderInfo in self.traders:
            trader: traderBot.TraderBot = traderInfo["trader"]
            print(f"{trader.get_name()} has {traderInfo['money']}$ and {traderInfo['stocks']} stocks")
            
    def generate_stock_price(self, value, deviation):
        chip = rnd.randint(-int(value * deviation), int(value * deviation))
        return value + chip