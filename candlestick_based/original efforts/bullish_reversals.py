# ou codeeeee

# standard candle info pattern , list of tuples for each candle [(open,close,high,low)]

def moving_average(l,n=10):
     return(sum(l[-n:])/n)

def trend(l):
     if moving_average(l)>moving_average(l[:-1]):
          return('uptrend')
     if moving_average(l)<moving_average(l[:-1]):
          return('down trend')
     else:
          return('side trend')


     

import yfinance as yf
import matplotlib.pyplot as plt

# Create a Yahoo Finance object for a specific stock (e.g., Apple)
stock = yf.Ticker('AAPL')

# Get historical stock data
historical_data = stock.history(period='1d', start='2023-10-20', end='2024-02-29')

# Do further analysis or processing with the data
print(" ")
#print(historical_data)
print(historical_data['Close'])
print(" ")

print(moving_average(historical_data['Close']))
print(trend(historical_data['Close']))


''' to plot the graph'''

historical_data['Close'].plot()
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()





        