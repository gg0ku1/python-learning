from flask import Flask, render_template

app = Flask(__name__)

fruits = [
    "Apple",
    "Banana",
    "Orange"
]

@app.route("/")
def home():
    return render_template(
    "index.html",
    fruits=fruits
)

app.run()

