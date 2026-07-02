from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("forms.html")

@app.route("/submit", methods = ["POST"])
def submit():
     name = request.form["name"]
     phone = request.form["phone"]
     email = request.form["email"]
     return redirect(url_for("home"))

@app.route("/home")
def home():

     return f"you've successfully sent information"

app.run()