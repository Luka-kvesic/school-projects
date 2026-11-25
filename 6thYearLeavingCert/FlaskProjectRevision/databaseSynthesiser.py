import sqlite3


db_connection = sqlite3.connect("Database.db")

cursor = db_connection.cursor()

createTable = """create table if not exists form(
id integer primary key autoincrement,
name text not null,
email text not null,
age integer,
experience text,
recommend text,
comment text
) STRICT"""

cursor.execute(createTable)
db_connection.commit()
