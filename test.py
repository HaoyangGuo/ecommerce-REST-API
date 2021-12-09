import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'kate', 'lmao')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'haoyang', 'dab'),
    (3, 'intern', 'lol')
]
cursor.executemany(insert_query, users)

connection.commit()

connection.close()
