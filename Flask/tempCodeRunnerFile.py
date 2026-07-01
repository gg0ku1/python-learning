from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("forms.html")

@app.route("/submit")
def submit():
     return "data submitted"

app.run()