import sqlite3

connectionDB = sqlite3.connect("iris_DB.db")

cursor = connectionDB.cursor()

createTable = """create table if not exists irisDB(
irisID integer primary key autoincrement,
sepalLength real not null,
sepalWidth real not null, 
petalLength real not null,
petalWidth real not null,
class integer not null
) STRICT
"""

addData = """insert into irisDB (sepalLength, sepalWidth, petalLength, petalWidth, class) values (?,?,?,?,?)"""

cursor.execute(createTable)

cvvFile = open('Iris - all-numbers.csv', 'r')
cvvFile.readline()
i =0
for line in cvvFile:
    line = line.strip("\n")
    line = line.split(",")
    i += 1
    print(i)
    for j in range(len(line)):
        num = float(line[j])
        line[j] = num
    line = tuple(line)
    
    cursor.execute(addData, line)
    print(line)
    connectionDB.commit()

cursor.close()
connectionDB.close()
    
