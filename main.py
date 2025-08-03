
from TradingBot import TradingBot
from PrepareData import load_data, plot_trades

def main():

    print("\n==============================================================================\n")
    print("Welcome to TradingBot Simulator!\n")
    print("You are able to choose any US stock or ETF and the TradingBot will buy or sell that stock/ETF using the historical market dataset (From 1983 to 2019).\n")
    print("The bot will complete the simulation process 3 times using 3 different algorithms:")
    print(" - Moving Average Crossover Strategy")
    print(" - RSI Strategy Trades")
    print(" - Bollinger Bands Strategy Trades")
    print("and output the final profits and total trades it has made.\n") 
    print("The TradingBot will then determine which algorithm generates the most profit and then visualize the buying/selling data of each algorithm.\n")
    print("==============================================================================\n")

    while True:
        
        # Asks for input of Stock/ETF ticker symbol to test
        print("Here is a list of all US stocks: https://www.tradingview.com/markets/stocks-usa/market-movers-all-stocks/")
        print ("Here is a list of all US ETFs: https://www.tradingview.com/etf-screener/\n")
        ticker_symbol = input("Enter the ticker symbol of any US stock or ETF you want to test (e.g. aapl or AAPL for Apple). To exit, type 'exit': \n").strip().lower()

        # Exits program if user types 'exit'
        if ticker_symbol == "exit":
            print("\nThank you for trying our TradingBot program. See you next time!\n\n(Exiting program)")
            break

        stock_to_test = ticker_symbol

        # Adds '.us' to match name in file
        if not stock_to_test.endswith('.us'):
            stock_to_test += '.us'

        print(f"\nChecking if '{ticker_symbol.upper()}' is a valid stock/ETF.\n")

        # Load prices for the selected stock/ETF
        prices, stock_df = load_data(stock_to_test)

        # Checks if stock/ETF is valid
        if stock_df.empty:
            print(f"No data found for ticker '{ticker_symbol.upper()}'. Please try again.\n")
            print("==============================================================================\n")
            continue

        print(f"Stock/ETF found! You selected: '{ticker_symbol.upper()}'\n")
        
        # Asks user to input a starting balance (must be positive)
        while True:
            try:
                starting_balance = float(input("Enter the bot's initial balance (must be a positive number): "))
                if starting_balance > 0:
                    break
                else:
                    print("Balance must be greater than 0. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        print("\n==============================================================================\n")

        # Runs the TradingBot Simulator
        print(f"Executing TradingBot Simulator for '{ticker_symbol.upper()}' with an Initial Balance of ${starting_balance}:")
        
        # Create separate bots for each algorithms
        bot_ma = TradingBot(starting_balance)
        bot_rsi = TradingBot(starting_balance)
        bot_bb = TradingBot(starting_balance)
        
        # Runs each TradingBot algorithm
        bot_ma.moving_average_crossover(prices)
        bot_rsi.rsi_strategy(prices)
        bot_bb.bollinger_bands_strategy(prices)
        
        # Print summary for each bot
        print("\n===================================RESULTS====================================\n")
        print("Moving Average Crossover Strategy")
        print(f"Final Balance: ${bot_ma.current_balance:.2f}")
        print(f"Total Trades: {bot_ma.total_trades}\n")
        
        print("RSI Strategy")
        print(f"Final Balance: ${bot_rsi.current_balance:.2f}")
        print(f"Total Trades: {bot_rsi.total_trades}\n")
        
        print("Bollinger Bands Strategy")
        print(f"Final Balance: ${bot_bb.current_balance:.2f}")
        print(f"Total Trades: {bot_bb.total_trades}\n")

        print("==============================================================================\n")
        
        # Calculates which algorithm has the highest ending balance
        balances = {
            "Moving Average Crossover": bot_ma.current_balance,
            "RSI": bot_rsi.current_balance,
            "Bollinger Bands": bot_bb.current_balance
        }

        best_algorithm = max(balances, key=balances.get)
        print(f"Best Strategy: {best_algorithm} with a final balance of ${balances[best_algorithm]:.2f}")

        # Plots the trades that each algorithm made
        print("\nThe visualization of the data will be shown: Exit the plot to continue.\n")
        print("==============================================================================\n")
        plot_trades(stock_df, bot_ma, bot_rsi, bot_bb, stock_to_test, starting_balance)


if __name__ == "__main__":
    main()
