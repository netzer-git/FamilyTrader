# FamilyTrader
Welcome to the Stock Exchange Bot Family Game! Yay!

In the game, we would each create a simple bot, with only 2 functions, that will play with the other bots at stock exchange trading. You can use this repository to try and run your bots, test and train it to the real competition we will all have in the future.

## Your Bot
Can I join?

Sure thing. You need to create your bot file in the Traders folder. Open a new Python file with your name, like Traders/Netzer.py, and add your bot inside. Finished your bot and you want to test it? Go to the testYourBot file, and follow the instructions! 

Each bot participating in the game should be a class inheriting from the TraderBot class, and so will have to include two functions.

You can see a few examples of trader bots in the Traders folders.

#### buy_offer(money: int, value: int, price: int, metadata: dict(string: any)) -> bool

This function takes the needed data and decides for the bot if it wants to buy the stock for the suggested price. The boolean value will need to be True for the bot to buy the stock, and False to not.

- money - the amount of available money the bot has at this point.
- value - current stock value.
- price - price suggested for this offer.
- metadata - a dictionary of multiple available values the game gives as metadata. Where the "current_day" key is changing daily and the "last_day" key will be the last day of the game.

Returning False will pass on the current offer, returning True will buy you the stocks, but only if you have enough money at this point.

#### sell_stocks(money: int, stocks: int, value: int, time: [int, int]) -> int

This function gets the current data of the bot and should decide how many (can be 0) stocks to sell at the current stock value.

- money - the amount of available money the bot has at this point.
- stocks - the amount of owned stocks the bot has at this point.
- value - current stock value.
- metadata - a dictionary of multiple available values the game gives as metadata. Where the "current_day" key changes daily and the "last_day" key will be the last day of the game.

Returning 0 will indicate no change. for any other number N, the bot will sell N stocks from the bot-owned stocks, gaining N*value money. On the last day, all bots need to sell all of their stock, since stocks do not worth anything at the end of the game.
## Day In The Exchange
For X traders, in a game that plays for Y days. Where the stock value is P
1. Randomize 2*X offers. Each trader gets 2 offers, for each offer, activate the bot on the buy_offer function for each offer.
2. (not in Alpha) In randomized turns, each trader will have the chance of buying each offer that no one has taken yet.
3. Each trader gets the option to sell any amount of stocks they have, as per the market value.
4. Price updating: goes up for each buy and down for each sell. Also moves around randomly.
