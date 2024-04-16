

# logic page

def three_black_crows(data):
    # data is a list of tuples with open and close of last 3 candles
    # data=[(o0, c0, h0, l0), (o1, c1, h1, l1), (o2, c2, h2, l2)]

    if data[0][0] > data[0][1] and data[1][0] > data[1][1] and data[2][0] > data[2][1] and data[0][0] > data[1][0] > data[2][0] and data[0][1] > data[1][1] > data[2][1]:
        return True
    else:
        return False


def three_white_soldiers(data):
    # data is a list of tuples with open and close of last 3 candles
    # data=[(o0, c0, h0, l0), (o1, c1, h1, l1), (o2, c2, h2, l2)]

    if data[0][0] < data[0][1] and data[1][0] < data[1][1] and data[2][0] < data[2][1] and data[0][0] < data[1][0] < data[2][0] and data[0][1] < data[1][1] < data[2][1]:
        return True
    else:
        return False


def evening_star(data):
    # data is a list of tuples with open and close of last 3 candles
    # data=[(o0, c0, h0, l0), (o1, c1, h1, l1), (o2, c2, h2, l2)]

    if data[0][0] < data[0][1] and data[1][1] < data[1][0] and data[2][1] < data[2][0] and data[0][0] < data[2][1] < data[1][1] and data[1][0] < data[0][1]:
        return True
    else:
        return False


def morning_star(data):
    # data is a list of tuples with open and close of last 3 candles
    # data=[(o0, c0, h0, l0), (o1, c1, h1, l1), (o2, c2, h2, l2)]

    if data[0][0] > data[0][1] and data[1][1] > data[1][0] and data[2][1] > data[2][0] and data[0][0] > data[2][1] > data[1][1] and data[0][1] < data[1][0]:
        return True
    else:
        return False


def golden_cross(data, short_window, long_window):
    # Calculate short and long-term moving averages
    short_ma = sum(data[-short_window:, 1]) / short_window  # Close prices for the last short_window days
    long_ma = sum(data[-long_window:, 1]) / long_window     # Close prices for the last long_window days

    # Generate signals based on the golden cross
    signal = 1 if short_ma > long_ma else 0

    return signal


def death_cross(data, short_window, long_window):
    # Calculate short and long-term moving averages
    short_ma = sum(data[-short_window:, 1]) / short_window  # Close prices for the last short_window days
    long_ma = sum(data[-long_window:, 1]) / long_window     # Close prices for the last long_window days

    # Generate signals based on the golden cross
    signal = 1 if short_ma < long_ma else 0

    return signal


def bearish_harami(data):
    if len(data) < 2:
        return False  # Need at least two days for pattern detection

    # Extracting the open and close prices of the last two days
    open_price_today, close_price_today, _, _ = data[-1]
    open_price_yesterday, close_price_yesterday, _, _ = data[-2]

    # Checking for bearish harami pattern
    if open_price_yesterday > close_price_yesterday and open_price_today < close_price_today and \
            open_price_today > close_price_yesterday and open_price_yesterday < close_price_today:
        return True
    else:
        return False


def bullish_harami(data):
    if len(data) < 2:
        return False  # Need at least two days for pattern detection

    # Extracting the open and close prices of the last two days
    open_price_today, close_price_today, _, _ = data[-1]
    open_price_yesterday, close_price_yesterday, _, _ = data[-2]

    # Checking for bullish harami pattern
    if open_price_yesterday < close_price_yesterday and open_price_today > close_price_today and \
            open_price_today < close_price_yesterday and open_price_yesterday > close_price_today:
        return True
    else:
        return False


def bearish_harami_cross(data):
    if len(data) < 3:
        return False  # Need at least three days for pattern detection

        # Extracting the open and close prices of the last three days
    _, close_price_today, _, _ = data[-1]
    open_price_yesterday, close_price_yesterday, _, _ = data[-2]
    open_price_day_before, close_price_day_before, _, _ = data[-3]

    # Checking for bearish harami cross pattern
    if open_price_day_before < close_price_day_before and \
            open_price_yesterday > close_price_yesterday and \
            open_price_yesterday == close_price_today and \
            open_price_yesterday > open_price_day_before and \
            close_price_today < open_price_day_before:
        return True
    else:
        return False


def bullish_harami_cross(data):
    if len(data) < 3:
        return False  # Need at least three days for pattern detection

    # Extracting the open and close prices of the last three days
    _, close_price_today, _, _ = data[-1]
    open_price_yesterday, close_price_yesterday, _, _ = data[-2]
    open_price_day_before, close_price_day_before, _, _ = data[-3]

    # Checking for bullish harami cross pattern
    if open_price_day_before > close_price_day_before and \
            open_price_yesterday < close_price_yesterday and \
            open_price_yesterday == close_price_today and \
            open_price_yesterday < open_price_day_before and \
            close_price_today > open_price_day_before:
        return True
    else:
        return False

'''import yfinance as yf
import matplotlib.pyplot as plt

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
start_date = '2023-01-01'
end_date = '2023-12-31'

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