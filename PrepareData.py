import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

# Loads data from CSV file
def load_data(stock_name):

    # Sets the folder and file name to find
    filename = f"historical_market_dataset/{stock_name}.csv"

    # If such file doesn't exist, return empty DataFrame
    if not os.path.exists(filename):
        return [], pd.DataFrame()
    
    # Loads CSV of given stock_name
    stock_df = pd.read_csv(filename)

    # Sorts the dates in ascending order
    stock_df["Date"] = pd.to_datetime(stock_df["Date"])
    stock_df = stock_df.sort_values(by="Date")

    # Prepares data as list of [Date, Price] pairs
    data = stock_df.loc[:, ["Date", "Close"]].copy()
    data.columns = ["Date", "Price"]
    stock_df = stock_df.sort_values(by="Date")
    
    # Converts to lists for passing into TradingBot algorithms
    data_list = data.values.tolist()
    
    # Returns the lists
    return data_list, stock_df


# Plots the trades using matplotlib
def plot_trades(stock_df, bot_ma, bot_rsi, bot_bb, stock_to_test, starting_balance):

    # Finds the algorithm with the highest balance and saves it
    balances = {
            "Moving Average Crossover": bot_ma.current_balance,
            "RSI": bot_rsi.current_balance,
            "Bollinger Bands": bot_bb.current_balance
        }
    
    best_algorithm = max(balances, key=balances.get)
    
    # Creates subplots: 3 rows for the 3 algorithms, 1 column
    fig, axes = plt.subplots(3, 1, figsize=(16, 12), sharex=True)

    strategies = [
        (r"$\bf{Moving\ Average\ Crossover}$" + f"\nFinal Balance: ${bot_ma.current_balance:,.2f}\nTotal Trades: {bot_ma.total_trades}", bot_ma),
        (r"$\bf{RSI\ Strategy}$" + f"\nFinal Balance: ${bot_rsi.current_balance:,.2f}\nTotal Trades: {bot_rsi.total_trades}", bot_rsi),
        (r"$\bf{Bollinger\ Bands}$" + f"\nFinal Balance: ${bot_bb.current_balance:,.2f}\nTotal Trades: {bot_bb.total_trades}", bot_bb)
    ]

    for ax, (title, bot) in zip(axes, strategies):
        # Plot the close prices
        ax.plot(stock_df["Date"], stock_df["Close"], label="Close Price", color='black', linewidth=1)

        # Extracts buys and sells from trade history
        buys = [t for t in bot.trade_history if t["type"] == "Buy"]
        sells = [t for t in bot.trade_history if t["type"] == "Sell"]

        # Plot buy points with green arrows pointing up
        ax.plot(
            [t["date"] for t in buys],
            [t["price"] for t in buys],
            marker = '^', color = 'green', linestyle = 'None', label = "Buy"
        )

        # Plot sell points with red arrows pointing down
        ax.plot(
            [t["date"] for t in sells],
            [t["price"] for t in sells],
            marker = 'v', color = 'red', linestyle = 'None', label = "Sell"
        )

        # Formats the plot
        ax.set_title(title)
        ax.set_ylabel("Price ($)")
        ax.legend()
        ax.grid(True)

    # Formats x-axis
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(36))
    plt.setp(axes[-1].xaxis.get_majorticklabels(), rotation=45, ha='right')

    # Sets x-axis lable
    axes[-1].set_xlabel("Date")
    display_name = stock_to_test.replace('.us', '')
    plt.suptitle(f"Bot's Trading Data for '{display_name.upper()}' with Initial Balance of ${starting_balance:,.2f}", fontsize = 16, fontweight = 'bold')


    # Adds best algorithm at the bottom
    plt.figtext(0.5, 0.02, f"Best Strategy: {best_algorithm} with a Final Balance of ${balances[best_algorithm]:,.2f}", 
    wrap = True, ha = 'center', fontsize=14, fontweight = 'bold')

    # Final formatting of plot
    plt.subplots_adjust(hspace = 0.9)
    plt.tight_layout(rect = [0, 0.05, 1, 0.96])
    plt.show()
