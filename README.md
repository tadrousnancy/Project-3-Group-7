# Trading Bot Simulator: Compare 3 Trading Algorithms

Welcome to the **Trading Bot Simulator**. This is a python project that allows the user to simulate trades using historical stock market data. The user is able to test **any U.S. stock or Exchange-Traded Fund (ETF)** and then compare the performance of three trading algorithms. 

## Features
 
- Test any U.S. stock or ETF using its ticker symbol (e.g. aapl or AAPL for Apple)
     - List of all US stocks: https://www.tradingview.com/markets/stocks-usa/market-movers-all-stocks/
     - List of all US Exchange-Traded Funds (ETFs): https://www.tradingview.com/etf-screener/
- Simulate and compare three trading algorithms:
     1. **Moving Average Crossover Algorithm**
     2. **Relative Strength Index (RSI) Algorithm**
     3. **Bollinger Bands Algorithm**
- Visualize buy/sell points on a historical price chart
- See final balances and trade counts for each algorithm
- Automatically identifies the most profitable algorithm 


## Project Structure 

- main.py: runs the user interface and simulator 
- TradingBot.py: contains the TradingBot class and 3 algorithms
- PrepareData.py: handles data loading and plotting
- historical_market_dataset folder: dataset 
- README.md 


## Dataset Setup

For this project, you’ll need pandas and matplotlib. 
Pandas: pip install pandas
Matplotlib: pip install matplotlib

Once everything is set up, you can run main.py. 

1. Enter a stock/ETF ticker. Links are included in the Features section to find tickers. 
2. Input your starting balance, which should be positive.
3. The results will appear in a new pop-up window.
4. A graph shows buy/sell actions for each algorithm, along with their final balance.
5. The program will determine which algorithm performed best, and its name will appear at the bottom of the window along with the final balance. 
