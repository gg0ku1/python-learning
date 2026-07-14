from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add", methods=["GET"])
def add_page():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    new_contact = {"name":name, "phone":phone, "email":email}
    contacts.append(new_contact)
    print(contacts)
    return redirect(url_for("home"))

@app.route("/contacts")
def view_page():
    return render_template("contacts.html", contacts = contacts)

@app.route("/delete/<int:index>")
def delete_page(index):
    del contacts[index]
    return redirect(url_for("view_page"))


if __name__ == "__main__":
    app.run(debug=True)

