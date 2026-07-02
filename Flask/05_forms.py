from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("forms.html")

@app.route("/submit", methods = ["POST"])
def submit():
     name = request.form["name"]
     phone = request.form["phone"]
     email = request.form["email"]

     return f"hello {name}"



app.run()