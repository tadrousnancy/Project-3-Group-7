# Trading Bot Simulator: Compare 3 Trading Algorithms

Welcome to the **Trading Bot Simulator**. This is a python project which allows the user to simulate trades using historical stock market data. The user is able to test **any U.S. stock or ETF** and then compare the performance of three trading algorithms. 

## Features
 
- Test any U.S. stock or ETF using its ticker symbol (e.g. aapl or AAPL for Apple)
- Simulate and compare three trading algorithms:
     1. **Moving Average Crossover Algorithm**
     2. **Relative Strength Index (RSI) Algorithm**
     3. **Bollinger Bands Algorithm**
- Visualize buy/sell points on a historical price chart
- See final balances and trade counts for each algorithm
- Automatically identifies the most profitable algorithm 


## Project Structure 

- main.py: runs the user interface and simulator 
- TradingBot.py: contains TradingBot class and algorithms
- PrepareData.py: handles data loading and plotting
- historical_market_dataset folder: dataset 
- README.md 


## Dataset Setup

For this project you’ll need pandas and matplotlib. 

Once everything is set up, you can run main.py. 

1. Enter a stock/ETF ticker. There are links included to find tickers. 
2. Input your starting balance
3. View results of all three algorithms.
4. Find which one performed best. 
5. A graph will pop up showing buy/sell actions for each algorithm.


