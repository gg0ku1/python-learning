import sqlite3

connection = sqlite3.connect(
    r"C:\Users\Gokul\Desktop\code\python-learning\instance\contacts.db"
)

cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

print(cursor.fetchall())

cursor.execute("SELECT * FROM User")

print(cursor.fetchall())

connection.close()