import pandas as pd

class TradingBot:
    def __init__(self, starting_balance):
        self.starting_balance = starting_balance
        self.current_balance = self.starting_balance
        self.position = 0
        self.total_trades = 0
        self.trade_history = []
        
    def buy(self, price):
          if self.position == 0:
            self.position = self.current_balance / price
            self.current_balance -= self.position * price
            self.total_trades += 1
            self.trade_history.append({"Buy": price})
            
    def sell(self, price):
         if self.position > 0:
            self.current_balance += self.position * price
            self.position = 0
            self.total_trades += 1
            self.trade_history.append({"Sell": price})

    def moving_average_crossover(self, data):
        prices = pd.DataFrame(data, columns=["Price"])

        prices["moving_average_20"] = prices["Price"].rolling(window=20).mean()
        prices["moving_average_50"] = prices["Price"].rolling(window=50).mean()

        for i in range(50, len(prices)):
            if prices["moving_average_20"].iloc[i] > prices["moving_average_50"].iloc[i]:
                self.buy(prices["Price"].iloc[i])
            elif prices["moving_average_50"].iloc[i] < prices["moving_average_50"].iloc[i]:
                self.sell(prices["Price"].iloc[i])

        '''
        if moving_average_20 > moving_average_50:
        self.buy(price)
        elif moving_average_20 < moving_average_50 and self.position > 0:
        self.sell(price)
        '''

    def rsi_strategy(self, data):
        prices = pd.DataFrame(data, columns=["Price"])

        prices["Change"] = prices["Price"].diff()
        prices["Gains"] = prices["Change"].where(prices["Change"] > 0, 0)
        prices["Losses"] = -prices["Change"].where(prices["Change"] < 0, 0)

        prices["average_gains"] = prices["Gains"].rolling(window=14).mean()
        prices["average_losses"] = prices["Losses"].rolling(window=14).mean()

        prices["RSI"] = 100 - (100 / (1 + (prices["average_gains"] / prices["average_losses"])))

        for i in range(14, len(prices)):
            if prices["RSI"].iloc[i] < 30:
                self.buy(prices["Price"].iloc[i])
            elif prices["RSI"].iloc[i] > 70 and self.position > 0:
                self.sell(prices["Price"].iloc[i])

        '''
        if RSI < 30:
            self.buy(price)

        if RSI > 70 and self.position > 0:
            self.sell(price)
        '''

    