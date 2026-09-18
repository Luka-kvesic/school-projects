import sqlite3

db_connection = sqlite3.connect("database.db")

cursor = db_connection.cursor()

createTable = '''create table if not exists playersDataBase(
id integer primary key autoincrement,
name text not null,
year integer,
appearances integer,
goals integer
) STRICT'''

cursor.execute(createTable)
db_connection.commit()



addData = '''insert into playersDataBase (name, year, appearances, goals) values (?,?,?,?)'''



spursFile = open("Spurs_Data.CSV","r")
spursFile.readline()
for line in spursFile:
    line = line.strip()
    db = tuple(line.split(","))
    cursor.execute(addData, db)
    db_connection.commit()


fetchData = '''select name, goals from playersDataBase'''
cursor.execute(fetchData)
for row in cursor:
    
    if row[0] != currentName:
        
    





cursor.close()
db_connection.close()



