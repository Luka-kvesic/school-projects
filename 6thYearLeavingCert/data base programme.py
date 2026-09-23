import sqlite3

DB_connection = sqlite3.connection("jobDataBaseFile.db")

cursor = DB_connection.cursor()

jobDataBase = '''create table if not exists jobDataBase(
id integer primary key autoincrement,
name text not null,
department text not null,
salary integer
) STRICT'''


cursor.execute(jobDataBase)

DB_connection.commit()

#data to be put into database
data = [["John Doe", "Engineeing", 75000],["Jane Smith", "HR", 60000],["Mike Johns", "Finance", 70000],["Sarah Brown", "Marketing", 65000],["Chris White", "Sales", 62000]]


for i in range(len(data)):
    name = data[i][0]
    department
    addData = '''insert into jobDataBase ()
