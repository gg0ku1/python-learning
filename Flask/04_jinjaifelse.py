from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    fruits = ["Apple", "Banana", "Orange"]

    return render_template(
        "index3.html",
        name="Gokul",
        age=22,
        fruits=fruits
    )

app.run()
