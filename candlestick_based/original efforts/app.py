'''from flask import Flask, redirect, url_for,render_template,request

app = Flask(__name__)


@app.route('/')

def home():
    return render_template('pict_1.html')


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")
@app.route("/<usr>")
def user(usr):
    return(f"<h1>{usr}</h1>")


if __name__ == '__main__':
    app.run(debug=True)'''


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        value = request.form['input_value']
        return render_template('result.html', value=value)
    else:
        return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run(debug=True)
