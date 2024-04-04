'''import yfinance as yf
import matplotlib.pyplot as plt

def identify_three_black_crows(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate daily returns
    stock_data['Daily_Return'] = stock_data['Close'].pct_change()

    # Identify Three Black Crows pattern
    three_black_crows = []
    for i in range(2, len(stock_data)-2):
        if stock_data['Close'][i] < stock_data['Open'][i] and \
           stock_data['Close'][i-1] < stock_data['Open'][i-1] and \
           stock_data['Close'][i-2] < stock_data['Open'][i-2] and \
           stock_data['Close'][i-1] < stock_data['Close'][i-2] and \
           stock_data['Close'][i] < stock_data['Close'][i-1]:
            three_black_crows.append(stock_data.index[i])'''

    
'''# Plotting the stock prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.title(f'{ticker_symbol} Stock Price with Three Black Crows Pattern')
    
    # Highlight Three Black Crows pattern
    for date in three_black_crows:
        plt.axvline(date, color='red', linestyle='--', linewidth=2, label='Three Black Crows')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2024-01-01'
end_date = '2024-02-29'
identify_three_black_crows(ticker_symbol, start_date, end_date)'''

'''
def identify_three_white_soldiers(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate daily returns
    stock_data['Daily_Return'] = stock_data['Close'].pct_change()

    # Identify Three White Soldiers pattern
    three_white_soldiers = []
    for i in range(2, len(stock_data)-2):
        if stock_data['Close'][i] > stock_data['Open'][i] and \
           stock_data['Close'][i-1] > stock_data['Open'][i-1] and \
           stock_data['Close'][i-2] > stock_data['Open'][i-2] and \
           stock_data['Close'][i-1] > stock_data['Close'][i-2] and \
           stock_data['Close'][i] > stock_data['Close'][i-1]:
            three_white_soldiers.append(stock_data.index[i])

    # Plotting the stock prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.title(f'{ticker_symbol} Stock Price with Three White Soldiers Pattern')
    
    # Highlight Three White Soldiers pattern
    for date in three_white_soldiers:
        plt.axvline(date, color='green', linestyle='--', linewidth=2, label='Three White Soldiers')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-12-31'

identify_three_white_soldiers(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt

def identify_bullish_harami(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate daily returns
    stock_data['Daily_Return'] = stock_data['Close'].pct_change()

    # Identify Bullish Harami pattern
    bullish_harami = []
    for i in range(1, len(stock_data)-1):
        if stock_data['Close'][i] < stock_data['Open'][i] and \
           stock_data['Close'][i-1] > stock_data['Open'][i-1] and \
           stock_data['Open'][i] < stock_data['Close'][i-1] and \
           stock_data['Close'][i] > stock_data['Open'][i-1]:
            bullish_harami.append(stock_data.index[i])

    # Plotting the stock prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.title(f'{ticker_symbol} Stock Price with Bullish Harami Pattern')
    
    # Highlight Bullish Harami pattern
    for date in bullish_harami:
        plt.axvline(date, color='green', linestyle='--', linewidth=2, label='Bullish Harami')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

identify_bullish_harami(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt

def identify_bearish_harami(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate daily returns
    stock_data['Daily_Return'] = stock_data['Close'].pct_change()

    # Identify Bearish Harami pattern
    bearish_harami = []
    for i in range(1, len(stock_data)-1):
        if stock_data['Close'][i] > stock_data['Open'][i] and \
           stock_data['Close'][i-1] < stock_data['Open'][i-1] and \
           stock_data['Open'][i] > stock_data['Close'][i-1] and \
           stock_data['Close'][i] < stock_data['Open'][i-1]:
            bearish_harami.append(stock_data.index[i])

    # Plotting the stock prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.title(f'{ticker_symbol} Stock Price with Bearish Harami Pattern')
    
    # Highlight Bearish Harami pattern
    for date in bearish_harami:
        plt.axvline(date, color='red', linestyle='--', linewidth=2, label='Bearish Harami')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

identify_bearish_harami(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt

def identify_death_cross(ticker_symbol, short_window=10, long_window=50, start_date=None, end_date=None):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate short and long moving averages
    stock_data['Short_MA'] = stock_data['Close'].rolling(window=short_window, min_periods=1).mean()
    stock_data['Long_MA'] = stock_data['Close'].rolling(window=long_window, min_periods=1).mean()

    # Identify Death Cross pattern
    death_cross = []
    for i in range(1, len(stock_data)):
        if stock_data['Short_MA'][i-1] > stock_data['Long_MA'][i-1] and \
           stock_data['Short_MA'][i] <= stock_data['Long_MA'][i]:
            death_cross.append(stock_data.index[i])

    # Plotting the stock prices and moving averages
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.plot(stock_data['Short_MA'], label=f'{short_window}-Day MA', color='orange')
    plt.plot(stock_data['Long_MA'], label=f'{long_window}-Day MA', color='green')
    plt.title(f'{ticker_symbol} Stock Price with Death Cross Pattern')
    
    # Highlight Death Cross pattern
    for date in death_cross:
        plt.axvline(date, color='red', linestyle='--', linewidth=2, label='Death Cross')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-12-31'

identify_death_cross(ticker_symbol, start_date=start_date, end_date=end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt

def identify_golden_cross(ticker_symbol, short_window=10, long_window=50, start_date=None, end_date=None):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate short and long moving averages
    stock_data['Short_MA'] = stock_data['Close'].rolling(window=short_window, min_periods=1).mean()
    stock_data['Long_MA'] = stock_data['Close'].rolling(window=long_window, min_periods=1).mean()

    # Identify Golden Cross pattern
    golden_cross = []
    for i in range(1, len(stock_data)):
        if stock_data['Short_MA'][i-1] < stock_data['Long_MA'][i-1] and \
           stock_data['Short_MA'][i] >= stock_data['Long_MA'][i]:
            golden_cross.append(stock_data.index[i])

    # Plotting the stock prices and moving averages
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.plot(stock_data['Short_MA'], label=f'{short_window}-Day MA', color='orange')
    plt.plot(stock_data['Long_MA'], label=f'{long_window}-Day MA', color='green')
    plt.title(f'{ticker_symbol} Stock Price with Golden Cross Pattern')
    
    # Highlight Golden Cross pattern
    for date in golden_cross:
        plt.axvline(date, color='green', linestyle='--', linewidth=2, label='Golden Cross')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-12-31'

identify_golden_cross(ticker_symbol, start_date=start_date, end_date=end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt

def identify_long_black_body(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Identify Long Black Body pattern
    long_black_body = []
    for i in range(len(stock_data)):
        if stock_data['Close'][i] < stock_data['Open'][i] and \
           abs(stock_data['Close'][i] - stock_data['Open'][i]) > 0.5 * (stock_data['High'][i] - stock_data['Low'][i]):
            long_black_body.append(stock_data.index[i])

    # Plotting the stock prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.title(f'{ticker_symbol} Stock Price with Long Black Body Pattern')
    
    # Highlight Long Black Body pattern
    for date in long_black_body:
        plt.axvline(date, color='black', linestyle='--', linewidth=2, label='Long Black Body')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

identify_long_black_body(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt

def identify_long_white_body(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Identify Long White Body pattern
    long_white_body = []
    for i in range(len(stock_data)):
        if stock_data['Close'][i] > stock_data['Open'][i] and \
           abs(stock_data['Close'][i] - stock_data['Open'][i]) > 0.5 * (stock_data['High'][i] - stock_data['Low'][i]):
            long_white_body.append(stock_data.index[i])

    # Plotting the stock prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.title(f'{ticker_symbol} Stock Price with Long White Body Pattern')
    
    # Highlight Long White Body pattern
    for date in long_white_body:
        plt.axvline(date, color='green', linestyle='--', linewidth=2, label='Long White Body')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

identify_long_white_body(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt

def identify_bullish_kicking(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Identify Bullish Kicking pattern
    bullish_kicking = []
    for i in range(1, len(stock_data)-1):
        if stock_data['Open'][i] < stock_data['Close'][i-1] and \
           stock_data['Close'][i] > stock_data['Open'][i] and \
           stock_data['Open'][i] < stock_data['Low'][i-1] and \
           stock_data['Close'][i] > stock_data['High'][i-1]:
            bullish_kicking.append(stock_data.index[i])

    # Plotting the stock prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.title(f'{ticker_symbol} Stock Price with Bullish Kicking Pattern')
    
    # Highlight Bullish Kicking pattern
    for date in bullish_kicking:
        plt.axvline(date, color='green', linestyle='--', linewidth=2, label='Bullish Kicking')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

identify_bullish_kicking(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt

def identify_bearish_kicking(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Identify Bearish Kicking pattern
    bearish_kicking = []
    for i in range(1, len(stock_data)-1):
        if stock_data['Open'][i] > stock_data['Close'][i-1] and \
           stock_data['Close'][i] < stock_data['Open'][i] and \
           stock_data['Open'][i] > stock_data['High'][i-1] and \
           stock_data['Close'][i] < stock_data['Low'][i-1]:
            bearish_kicking.append(stock_data.index[i])

    # Plotting the stock prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.title(f'{ticker_symbol} Stock Price with Bearish Kicking Pattern')
    
    # Highlight Bearish Kicking pattern
    for date in bearish_kicking:
        plt.axvline(date, color='red', linestyle='--', linewidth=2, label='Bearish Kicking')

    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

identify_bearish_kicking(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt
import server

def calculate_kd_ratio(ticker_symbol, start_date, end_date, window=14):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate %K and %D
    stock_data['Lowest Low'] = stock_data['Low'].rolling(window=window).min()
    stock_data['Highest High'] = stock_data['High'].rolling(window=window).max()
    stock_data['%K'] = (stock_data['Close'] - stock_data['Lowest Low']) / (stock_data['Highest High'] - stock_data['Lowest Low']) * 100
    stock_data['%D'] = stock_data['%K'].rolling(window=3).mean()

    # Plotting %K and %D
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['%K'], label='%K', color='blue')
    plt.plot(stock_data['%D'], label='%D', color='red')
    plt.title(f'{ticker_symbol} Stochastic Oscillator (%K and %D)')
    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = server.name1#'2023-01-01'
end_date = server.name2#'2023-12-31'

calculate_kd_ratio(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def calculate_mfi(data, period=14):
    typical_price = (data['High'] + data['Low'] + data['Close']) / 3
    money_flow = typical_price * data['Volume']
    
    positive_flow = (typical_price.diff() > 0).values * money_flow.values
    negative_flow = (typical_price.diff() < 0).values * money_flow.values

    positive_mf = pd.Series(positive_flow).rolling(window=period, min_periods=0).sum()
    negative_mf = pd.Series(negative_flow).rolling(window=period, min_periods=0).sum()

    mfi = 100 - (100 / (1 + (positive_mf / negative_mf)))
    return mfi

def plot_mfi(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate MFI
    mfi = calculate_mfi(stock_data)

    # Plotting the MFI
    plt.figure(figsize=(10, 6))
    plt.plot(mfi, label='MFI', color='blue')
    plt.axhline(20, linestyle='--', color='red')
    plt.axhline(80, linestyle='--', color='green')
    plt.title(f'Money Flow Index (MFI) for {ticker_symbol}')
    plt.xlabel('Date')
    plt.ylabel('MFI')
    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

plot_mfi(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def calculate_coppock_curve(data, roc1_period=14, roc2_period=11, wma_period=10):
    # Calculate Rate of Change (ROC)
    data['ROC1'] = data['Close'].pct_change(roc1_period)
    data['ROC2'] = data['Close'].pct_change(roc2_period)

    # Calculate Coppock Curve
    data['Coppock_Curve'] = data['ROC1'] + data['ROC2']
    data['Coppock_Curve'] = data['Coppock_Curve'].ewm(span=wma_period, adjust=False).mean()

    return data

def plot_coppock_curve(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate Coppock Curve
    stock_data = calculate_coppock_curve(stock_data)

    # Plotting the Coppock Curve
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Coppock_Curve'], label='Coppock Curve', color='blue')
    plt.title(f'{ticker_symbol} Coppock Curve')
    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

plot_coppock_curve(ticker_symbol, start_date, end_date)'''

'''import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def calculate_awesome_oscillator(data):
    # Calculate simple moving averages
    sma_5 = data['Close'].rolling(window=5).mean()
    sma_34 = data['Close'].rolling(window=34).mean()
    
    # Calculate Awesome Oscillator
    ao = sma_5 - sma_34
    return ao

def plot_awesome_oscillator(ticker_symbol, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate Awesome Oscillator
    ao = calculate_awesome_oscillator(stock_data)

    # Plotting the Awesome Oscillator
    plt.figure(figsize=(10, 6))
    plt.plot(ao, label='Awesome Oscillator', color='blue')
    plt.axhline(0, linestyle='--', color='gray')
    plt.title(f'Awesome Oscillator for {ticker_symbol}')
    plt.xlabel('Date')
    plt.ylabel('Awesome Oscillator')
    plt.legend()
    plt.show()

# Example usage
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

plot_awesome_oscillator(ticker_symbol, start_date, end_date)'''