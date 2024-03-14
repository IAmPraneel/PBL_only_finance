from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
  global name1, name2
  if request.method == "GET":
    # Send initial form to the user
    return render_template("index.html")  # Specify the correct template filename
  elif request.method == "POST":
    # Get data from the form
    name = request.form.get("name")
    name1 = request.form.get("name1")
    name2 = request.form.get("name2")

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
        start_date = name1#'2023-01-01'
        end_date = name2#'2023-12-31'

        plot_awesome_oscillator(ticker_symbol, start_date, end_date)
    # Process or store the received data (name and message)
        processed_message = f"Hello, {name}! start date: {name1} end date: {name2}"
    # Send the processed information back to the user
        return render_template("response.html", processed_message=processed_message)

if __name__ == "__main__":
  app.run(debug=True)










  
