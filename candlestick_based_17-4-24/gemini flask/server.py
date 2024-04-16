'''from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#import finrun as fn

app = Flask(__name__, template_folder="templates")'''
'''
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
    return render_template("response.html", processed_message=processed_message)'''

'''@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # Send initial form to the user
        return render_template("index.html")
    elif request.method == "POST":
        # Get data from the form
        Ticker = request.form.get("Ticker")
        date1 = request.form.get("date1")
        date2 = request.form.get("date2")
        indnum = request.form.get("indnum")

        # Check if all required fields are filled
        if not Ticker or not date1 or not date2 or not indnum:
            error_message = "Please fill in all the fields."
            return render_template("index.html", error_message=error_message)

        # Process the received data
        processed_message = f"Hello, {Ticker}! Start date: {date1}, End date: {date2}, Ticker number: {indnum}"
        
        # Debug statement
        print(f"Processed message: {processed_message}")

        # Send the processed information back to the user
        return render_template("response.html", processed_message=processed_message)


if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
  app.run(debug=True)
  
  # do(Ticker,date1,date2,n)
  #fn.do(Ticker,date1,date2,indnum)'''

from flask import Flask, render_template, request
from finrun import fincall

from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder="templates")

'''@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # Send initial form to the user
        return render_template("index.html")
    elif request.method == "POST":
        # Get data from the form
        Ticker = request.form.get("Ticker")
        date1 = request.form.get("date1")
        date2 = request.form.get("date2")
        indnum = request.form.get("indnum")

        # Check if all required fields are filled
        if not Ticker or not date1 or not date2 or not indnum:
            error_message = "Please fill in all the fields."
            return render_template("index.html", error_message=error_message)

        # Process the received data
        fincall(Ticker,date1,date2,indnum)
        # Clear the current figure
        plt.clf()


        # Save the plot to a bytes object
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        img_encoded = base64.b64encode(img.getvalue()).decode()
        processed_message = f"Hello, {Ticker}! Start date: {date1}, End date: {date2}, Ticker number: {indnum}"
        
        # Debug statement
        print(f"Processed message: {processed_message}")

        # Send the processed information back to the user
        return render_template("response.html", processed_message=processed_message,img=img_encoded)
'''
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # Send initial form to the user
        return render_template("index.html")
    elif request.method == "POST":
        # Get data from the form
        Ticker = request.form.get("Ticker")
        date1 = request.form.get("date1")
        date2 = request.form.get("date2")
        indnum = request.form.get("indnum")

        # Check if all required fields are filled
        if not Ticker or not date1 or not date2 or not indnum:
            error_message = "Please fill in all the fields."
            return render_template("index.html", error_message=error_message)

        # Process the received data
        img=fincall(Ticker,date1,date2,indnum)
        img_encoded = base64.b64encode(img.getvalue()).decode('utf-8')
        # Save the plot to a bytes object
        '''img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        img_encoded = base64.b64encode(img.getvalue()).decode()'''
        processed_message = f"Hello, {Ticker}! Start date: {date1}, End date: {date2}, Ticker number: {indnum}"
        
        # Debug statements
        

        # Send the processed information back to the user
        return render_template("response.html", processed_message=processed_message, img=img_encoded)

if __name__ == "__main__":
    app.run(debug=True)








  
