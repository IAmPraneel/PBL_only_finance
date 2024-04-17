from flask import Flask, render_template, request
from finrun import fincall
import base64
import matplotlib
matplotlib.use('Agg')
app = Flask(__name__, template_folder="templates")
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
        img = base64.b64encode(img).decode()
        # Save the plot to a bytes object
        processed_message = f"Ticker selected : {Ticker}! Start date: {date1}, End date: {date2}, Indicator number: {indnum}"
        # Send the processed information back to the user
        return render_template("response.html", processed_message=processed_message, img=img)
@app.route("/to_home")
def to_home():
    return render_template("home.html")
@app.route("/to_route")
def to_indicator():
    return render_template("indicator.html")

if __name__ == "__main__":
    app.run(debug=True)








  
