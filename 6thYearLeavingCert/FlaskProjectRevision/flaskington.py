from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)

@app.route("/")

def homePage():
    return render_template("Home.html")
@app.route("/index")

def surveyPage():
    return render_template("index.html")

@app.route("/results")
def resultsPage():
    return render_template("results.html")

addData = """insert into form (name, email, age, experience, recommend, comment) values (?,?,?,?,?,?)"""


@app.route("/FormTaker", methods=["POST"])
def FormTaker():
    data = dict(request.form)
    print(data)
    db_connection = sqlite3.connect("Database.db")
    cursor = db_connection.cursor()
    cursor.execute(addData, (data["name"], data["email"], data["age"], data["experience"], data["recommend"], data["comment"], ))
    db_connection.commit()
    return render_template("results.html")
    

