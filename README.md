# FamilyTrader

## Day In The Exchange
For X traders, in a game that plays for Y days. Where the stock value is P
1. Randomize 2*X offers for the price of 
2. Each trader get 2 offers, for each offer, activate the bot on buy_offer function.
3. (not in Alpha) In randomize turns, each trader will have the chance of buying each offer that no one have taken yet.
4. Each trader gets the option to sell any amount of stocks they have, as per the market value.
5. Price updating: goes up for each buy and down for each sell. Also moves around randomly.

## Your Bot
Each bot participating in the game should be a class inheriting from the TraderBot class, and so will have to include two functions:

#### buy_offer(money: int, value: int, price: int, time: [int, int]) -> bool

This function takes the need data and decide for the bot if it want to buy the stock for the suggested price. The boolean value will need to be True for the bot to buy the stock, and False to not.

- money - amount of available money the bot have at this point.
- value - current stock value.
- price - price suggested for this offer.
- time - a list of [current_day, last_day] where current_day is changing every day and last_day will be the last day of the game.

Returning False will pass on the current offer, returning True will buy you the stocks, but only if you have enough money at this point.

#### sell_stocks(money: int, stocks: int, value: int, time: [int, int]) -> int

This function gets the current data of the bot, and should decide how many (can be 0) stocks to sell at the current stock value.

- money - amount of available money the bot have at this point.
- stocks - amount of owned stocks the bot have at this point.
- value - current stock value.
- time - a list of [current_day, last_day] where current_day is changing every day and last_day will be the last day of the game.

Returning 0 will indicate no change. for any other number N, the bot will sell N stocks from the bot owned stocks, gaining N*value money. In the last day, all bots need to sell all of their stock, since stocks do not worth anything at the end of the game.