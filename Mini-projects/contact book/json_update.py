import json

contacts = [
    {
        "name": "Alice",
        "phone": 12345
    }
]

with open("alice.json", "w") as file:
    json.dump(contacts, file)

with open("alice.json", "r") as file:
    book = json.load(file)

print(book)