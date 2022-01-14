import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

create_users = "create table if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_users)

create_items = "create table if not exists items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_items)


insert_item = "insert into items values(null, 'test', 20.0)"
cursor.execute(insert_item)

connection.commit()
connection.close()
