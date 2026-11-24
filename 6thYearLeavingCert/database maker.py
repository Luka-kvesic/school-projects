import sqlite3


DB_connection = sqlite3.connect("database.db")
cursor = DB_connection.cursor()

createTable = """create table if not exists users(
id integer primary key autoincrement,
name text not null,
sex text,
country text not null,
message text,
newsletter text
) STRICT"""

cursor.execute(createTable)
DB_connection.commit()