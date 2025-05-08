import sqlite3

# define connection and cursor

connection = sqlite3.connect('books.db')

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS books")

command1 = '''CREATE TABLE IF NOT EXISTS
books(book_id INTEGER PRIMARY KEY, name TEXT, author_name TEXT, pages INTEGER, reading_time INTEGER)'''

cursor.execute(command1)

#add to book data

cursor.execute("INSERT INTO books VALUES (1, 'Normal People', 'Sally Rooney', 300, 7 )")
cursor.execute("INSERT INTO books VALUES (2, 'Diune', 'Frank Herbert', 600, 10)")

#get result

cursor.execute("SELECT * FROM books")

results = cursor.fetchall()
print(results)

connection.commit()
connection.close()
