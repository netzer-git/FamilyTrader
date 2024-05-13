# you finished with your bot? GREAT! Let's give it a try!
# You are welcome to edit and run this file, but don't check the results in!

# 1. Go to Traders/__init__ and add an import line to your bot, look at the comments their for instructions

# 2. Add your own import here! it should look like this
from Traders import emptyTrader

# 3. Now add your own bot instance to the traders list
# Adding multiple bots instances to this list will run all of them together
traders = [
    # like this
    emptyTrader.EmptyTrader()
]

from main import stock_exchange_wrapper
# 4. That's it! Now we can run the simulation!
stock_exchange_wrapper(traders, debug=True)