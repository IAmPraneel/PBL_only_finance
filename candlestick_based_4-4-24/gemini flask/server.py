from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

import finrun as fn

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
  global Ticker, date1, date2, indnum
  if request.method == "GET":
    # Send initial form to the user
    return render_template("index.html")  # Specify the correct template filename
  elif request.method == "POST":
    # Get data from the form
    Ticker = request.form.get("Ticker")
    date1 = request.form.get("date1")
    date2 = request.form.get("date2")
    indnum=request.form.get('indnum')

    # Process or store the received data (name and message)
    processed_message = f"Hello, {Ticker}! start date : {date1} end date : {date2} Ticker number : {indnum}"
    # Send the processed information back to the user
    return render_template("response.html", processed_message=processed_message)

if __name__ == "__main__":
  app.run(debug=True)
  
  # do(Ticker,date1,date2,n)
  #fn.do(Ticker,date1,date2,indnum)








  
