import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Loads data from CSV file
def load_data(filename, stock_name):

    # Loads full CSV
    df = pd.read_csv(filename)
    
    # Filter rows for the given stock (Name column)
    stock_df = df[df["Name"] == stock_name].copy()

    # Prepares data as list of [Date, Price] pairs
    data = stock_df.loc[:, ["Date", "Close"]].copy()
    data.columns = ["Date", "Price"]
    
    # Converts to lists for passing into TradingBot algorithms
    data_list = data.values.tolist()
    
    return data_list, stock_df

# Plots the trades using matplotlib
def plot_trades(stock_df, bot_ma, bot_rsi, bot_bb, stock_to_test):

    # Creates subplots: 3 rows for the 3 algorithms, 1 column
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

    strategies = [
        ("Moving Average Crossover", bot_ma),
        ("RSI Strategy", bot_rsi),
        ("Bollinger Bands", bot_bb)
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
            marker='^', color='green', linestyle='None', label="Buy"
        )

        # Plot sell points with red arrows pointing down
        ax.plot(
            [t["date"] for t in sells],
            [t["price"] for t in sells],
            marker='v', color='red', linestyle='None', label="Sell"
        )

        ax.set_title(title)
        ax.set_ylabel("Price ($)")
        ax.legend()
        ax.grid(True)

    # Formats x-axis
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(36))

    # Sets x-axis lable
    axes[-1].set_xlabel("Date")
    display_name = stock_to_test.replace('.us', '')
    plt.suptitle(f"Bot's Trading Data for '{display_name.upper()}'", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

