from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"

app.run()