import sqlite3

DB_connection = sqlite3.connect("jobDataBaseFile.db")

cursor = DB_connection.cursor()

CreateJobDataBase = '''create table if not exists jobDataBase(
id integer primary key autoincrement,
name text not null,
department text not null,
salary integer
) STRICT'''


cursor.execute(CreateJobDataBase)

DB_connection.commit()

#data to be put into database
data = [["John_Doe", "Engineeing", 75000],["Jane_Smith", "HR", 60000],["Mike_Johns", "Finance", 70000],["Sarah_Brown", "Marketing", 65000],["Chris_White", "Sales", 62000]]


for i in range(len(data)):
    name = data[i][0]
    department = data[i][1]
    salary = data[i][2]
    addData = '''insert into jobDataBase (name,department,salary) values (?,?,?)'''
    cursor.execute(addData, (name,department,salary))
    DB_connection.commit()


fetchData = '''select name, department, salary from jobDataBase'''
cursor.execute(fetchData)
for row in cursor:
    print(row)
    
    
cursor.close()
DB_connection.close()

