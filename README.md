# Trading Bot Simulator: Compare Trading Strategies 

Welcome to the **Trading Bot Simulator**. This is a python project which allows the user to simulate trades using historical stock market data. The user is able to test **any U.S. stock or ETF** and then compare the performance of three trading algorithms. 

## Features
 
- Test any U.S. stock or ETF using its ticker symbol (e.g. aapl for Apple)
- Simulate and compare three trading strategies:
     1. **Moving Average Crossover**
     2. **RSI Strategy**
     3. **Bollinger Bands Strategy**
- Visualize buy/sell points on a historical price chart
- See final balances and trade counts for each algorithm
- Automatically identifies the most profitable strategy 


## Project Structure 

- main.py: runs the user interface and simulator 
- TradingBot.py: contains TradingBot class and strategy algorithms
- PrepareData.py: handles data loading and plotting
- huge_stock_market_dataset.csv: required dataset (see Dataset Setup below)
- README.md 


## Dataset Setup

For this project you’ll need pandas and matplotlib. 

The Trading Bot uses a large historical stock market dataset (huge_stock_market_dataset.csv) that cannot be uploaded to GitHub due to file size limits.

###  Download the CSV file:

Please download it from the following link:
https://drive.google.com/file/d/1TCs-vnBpsizkk__0lbY7XL741PRwBjyX/view?usp=sharing

###  Place the File Here:

After downloading, move the file into the root directory of the project.

Once everything is set up, you can run main.py. 

1. Enter a stock/ETF ticker. There are links included to find tickers. 
2. Input your starting balance
3. View results of all three strategies.
4. Find which one performed best. 
5. A graph will pop up showing buy/sell actions for each algorithm.


