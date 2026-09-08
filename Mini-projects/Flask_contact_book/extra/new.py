import sqlite3

connection = sqlite3.connect(r"instance\contacts.db")
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(contact)")
print(cursor.fetchall())

connection.close()