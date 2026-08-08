import sqlite3

def create_database():
    connection = sqlite3.connect("contacts.db")

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

    connection.close()

def add_contact(name, phone, email):
    connection = sqlite3.connect("contacts.db")

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO contacts
    (name, phone, email)
    VALUES
    (?,?,?)
    """,
    (name, phone, email))

    connection.commit()

    connection.close()

def get_contacts():

    connection = sqlite3.connect("contacts.db")

    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    connection.close()

    return rows

def delete_contact(id):
    connection = sqlite3.connect("contacts.db")

    cursor = connection.cursor()

    cursor.execute(
    """
    DELETE FROM contacts
    WHERE id = ?
    """,
    (id,)
)
    

    connection.commit()
    connection.close()
