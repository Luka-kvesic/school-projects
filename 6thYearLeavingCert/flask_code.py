from flask import Flask, render_template, url_for, request
import sqlite3
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')
@app.route("/about") 
def about_page():
    return render_template("about.html")

@app.route('/forms_test')
def forms_test():
    return render_template("forms_test.html")

DB_connection = sqlite3.connect("database.db")
cursor = DB_connection.cursor()

addData = """
insert into users (name, sex, country, message, newsletter) values (?,?,?,?,?)
"""

@app.route('/receive_form_data', methods=["POST"])
def receive_form_data():
    data = request.form
    data = dict(data)
    cursor.execute(addData, (data["name"], data["sex"],data["country"],data["message"],data["newsletter"]))
    print(dict(data))
    return "Apple"

if __name__ == "__main__":
    app.run()