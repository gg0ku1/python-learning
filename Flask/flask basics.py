from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html" , 
                           name = "GOK")# dynamic variable



@app.route("/about")
def about():
    return "This is the About page."

app.run(debug=True)