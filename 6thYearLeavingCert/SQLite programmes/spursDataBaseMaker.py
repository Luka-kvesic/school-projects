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


fetchData = '''select name, appearances, goals from playersDataBase'''
cursor.execute(fetchData)
nameCount = 0
i = 1
firstIteration = True
appearanceAverageTotal = 0
for row in cursor:
    
    if firstIteration:
        currentName = row[0]
        firstIteration = False
    if row[0] != currentName:
        goalAverage = appearanceAverageTotal / i
        pastName = currentName
        print(pastName, "scored on average:", goalAverage, "goals per match")
        currentName = row[0]
        i = 0
        nameCount += 1
        appearanceAverageTotal = 0
    appearanceAverageTotal += row[2] / row[1]
    i += 1
goalAverage = appearanceAverageTotal / i
pastName = currentName
print(pastName, "scored on average: ", goalAverage, "goals per match")
    
    





cursor.close()
db_connection.close()



