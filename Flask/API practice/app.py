from flask import Flask, jsonify

app = Flask(__name__)

contacts = [
        {
            "id": 1,
            "name": "John",
            "phone": "9876543210"
        },
        {
            "id": 2,
            "name": "Sarah",
            "phone": "9123456780"
        }
    ]


@app.route("/api/contacts")
def get_contacts():

    return jsonify(contacts)

@app.route("/api/contacts/<int:id>")
def get_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            return jsonify(contact)

    return jsonify({"error": "Contact not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)