import sqlite3
connection = sqlite3.connect("contacts.db")

print("Database connected!")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT
)
""")

connection.commit()

cursor.execute("""
INSERT INTO contacts
(name, phone, email)
VALUES
("Alice","12345","alice@gmail.com")
""")

cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()

for row in rows:
    print(f"id:{row[0]} \n name:{row[1]} \n phone:{row[2]}\n email:{row[3]}")

connection.close()

#ok