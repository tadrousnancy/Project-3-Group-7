import pandas as pd

class TradingBot:
    def __init__(self, starting_balance):
        self.starting_balance = starting_balance
        self.current_balance = self.starting_balance
        self.position = 0
        self.total_trades = 0
        self.trade_history = []
        
    def buy(self, price, date=None):
          if self.position == 0:
            self.position = self.current_balance / price
            self.current_balance -= self.position * price
            self.total_trades += 1
            self.trade_history.append({"type": "Buy", "price": price, "date": date})
            
    def sell(self, price, date=None):
         if self.position > 0:
            self.current_balance += self.position * price
            self.position = 0
            self.total_trades += 1
            self.trade_history.append({"type": "Sell", "price": price, "date": date})

    def moving_average_crossover(self, data):
        prices = pd.DataFrame(data, columns=["Date", "Price"])

        prices["moving_average_20"] = prices["Price"].rolling(window=20).mean()
        prices["moving_average_50"] = prices["Price"].rolling(window=50).mean()

        for i in range(50, len(prices)):
            if prices["moving_average_20"].iloc[i] > prices["moving_average_50"].iloc[i]:
                self.buy(prices["Price"].iloc[i], prices["Date"].iloc[i])
            elif prices["moving_average_20"].iloc[i] < prices["moving_average_50"].iloc[i]:
                self.sell(prices["Price"].iloc[i], prices["Date"].iloc[i])

        if self.position > 0:
            self.sell(prices["Price"].iloc[-1], prices["Date"].iloc[-1])


    def rsi_strategy(self, data):
        prices = pd.DataFrame(data, columns=["Date", "Price"])

        prices["Change"] = prices["Price"].diff()
        prices["Gains"] = prices["Change"].where(prices["Change"] > 0, 0)
        prices["Losses"] = -prices["Change"].where(prices["Change"] < 0, 0)

        prices["average_gains"] = prices["Gains"].rolling(window=14).mean()
        prices["average_losses"] = prices["Losses"].rolling(window=14).mean()

        prices["RSI"] = 100 - (100 / (1 + (prices["average_gains"] / prices["average_losses"])))

        for i in range(14, len(prices)):
            if prices["RSI"].iloc[i] < 30:
                self.buy(prices["Price"].iloc[i], prices["Date"].iloc[i])
            elif prices["RSI"].iloc[i] > 70 and self.position > 0:
                self.sell(prices["Price"].iloc[i], prices["Date"].iloc[i])
        
        if self.position > 0:
            self.sell(prices["Price"].iloc[-1], prices["Date"].iloc[-1])

    
    def bollinger_bands_strategy(self, data):
        prices = pd.DataFrame(data, columns=["Date", "Price"])

        # calculating 20 day moving average and standard deviation
        prices["MA20"] = prices["Price"].rolling(window=20).mean()
        prices["STD20"] = prices["Price"].rolling(window=20).std()

        # calculating Bollinger Bands
        prices["UpperBand"] = prices["MA20"] + (2 * prices["STD20"])
        prices["LowerBand"] = prices["MA20"] - (2 * prices["STD20"])
 
        # The Trading logic
        for i in range(20, len(prices)):
            price = prices["Price"].iloc[i]
            date = prices["Date"].iloc[i]
            upper = prices["UpperBand"].iloc[i]
            lower = prices["LowerBand"].iloc[i]

            if price < lower:
                self.buy(price, date)
            elif price > upper and self.position > 0:
                self.sell(price, date)

        if self.position > 0:
            self.sell(prices["Price"].iloc[-1], prices["Date"].iloc[-1])
    

