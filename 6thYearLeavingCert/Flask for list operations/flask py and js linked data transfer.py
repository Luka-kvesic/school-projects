#use flask to be our server and send/receive data from website/database
from flask import Flask, render_template, url_for, request
#initialise constructor
app = Flask(__name__)
import sqlite3

connect_to_db = sqlite3.connect('iris.db')

db_cursor = connect_to_db.cursor()


get_data_from_db = """
select sepal_length, petal_length from irisData;
"""

db_cursor.execute(get_data_from_db)
data = db_cursor.fetchall()

#Every webpage will have an @app.route()with the name of the webpage inside
#the brackets
#the home page, usually called index.html, just has a forward slash
@app.route('/')
#This function is called, it will run what ever code we write
def some_function_name():
    #list1 = [(1,2,57),(4,3)]
    #This is the webpage we wish to launch in the browser
    #and the second argument is data we will pass to the webpage
    return render_template('index.html',list1=data)

#Run the app if this is the main file
if __name__ == "__main__":
  app.run()
