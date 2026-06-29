from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index2.html",
        name="Gokul",
        age=22,
        city="Pune"
    )

app.run()