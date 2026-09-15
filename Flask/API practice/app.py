from flask import Flask, jsonify, request

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

@app.route("/api/contacts/<int:id>", methods=["GET", "PUT","DELETE"])
def get_contact(id):

    if request.method == "PUT":
        data = request.get_json()

        for contact in contacts:
            if contact["id"] == id:
                contact["name"] = data["name"]
                contact["phone"] = data["phone"]
                return jsonify(contact)

        return jsonify({"error": "Contact not found"}), 404


    for contact in contacts:
        if contact["id"] == id:
            return jsonify(contact)

    return jsonify({"error": "Contact not found"}), 404

@app.route("/api/contacts", methods=["POST"])
def create_contact():
    data = request.get_json()

    new_id = len(contacts) + 1

    new_contact = {
        "id": new_id,
        "name": data["name"],
        "phone": data["phone"]
    }

    contacts.append(new_contact)

    return jsonify(new_contact), 201

if __name__ == "__main__":
    app.run(debug=True)