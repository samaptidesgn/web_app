from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
import sqlite3
import datetime
from math import cos, sin

app = Flask(__name__)
app.secret_key = "secret.key"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

Weight = ["Kg", "Lb"]
Database = "users.db"

def db_conn():
    db = sqlite3.connect(Database)
    db.row_factory = sqlite3.Row
    return db

def indb():
    db = db_conn()
    cur = db.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        hash TEXT NOT NULL
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS home (
        unid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id INTEGER NOT NULL,
        date DATE NOT NULL,
        mode TEXT NOT NULL,
        start TIME NOT NULL,
        end TIME NOT NULL,
        weight NUMBER NOT NULL,
        unit TEXT NOT NULL,
        energy NUMBER NOT NULL,
        dur NUMBER NOT NULL
    )
    ''')

    db.commit()
    db.close()


indb()


@app.route("/")
def index():
    return render_template("index.html")


# LOG IN ROUTE

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html")
    
    else:
        name = request.form.get("name")
        passw = request.form.get("password")

        # checking the user inputs
        if not name or not passw:
            return render_template("apology.html")
        
        # connecting database and checking if it is a valid user
        db = db_conn()
        rows = db.execute('SELECT id FROM user WHERE name = ? AND password = ?', (name, passw,)).fetchone()

        # if a valid user then storing the id of the user for further process in that particular account
        if rows:
            row = rows["id"]
            session["id"] = row
        else:
            return render_template("apology.html")
        
        # redirecting to the progress page
        return redirect("/progress")


# REGISTER ROUTE

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        passw = request.form.get("password")
        hash = request.form.get("hash")

        # checking if the name, password and confirmed password has not been entered
        if not name or not passw or not hash:
            return render_template("apology.html")
        if passw != hash:
            return render_template("apology.html")
        
        # hashing the password
        hash = "#"+ hash

        # checking if name is already taken if no then storing the info in Users database
        db = db_conn()
        rows = db.execute('SELECT * FROM user WHERE name = ?', (name,)).fetchall()
        if len(rows) != 0:
            return render_template("apology.html")

        db.execute('INSERT INTO user (name, password, hash) VALUES (?, ?, ?)', (name, passw, hash))
    
        db.commit()
        db.close()

        return redirect("/login")
    

# LOG OUT ROUTE

@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")



@app.route("/progress", methods=["GET", "POST"])
def progress():
    activities = []
    if request.method == "GET":
        return render_template("progress.html", activities=activities)
    else:
        sleep = request.form.get("sleep")
        meals = request.form.get("meals")
        chrs = request.form.get("chrs")
        work = request.form.get("work")
        reading = request.form.get("reading")
        exercise = request.form.get("exercise")
        others = request.form.get("others")

        if not sleep or not meals or not chrs or not work or not reading or not exercise or not others:
            return render_template("apology.html")
        
        else:
            sleep = float(sleep)
            meals = float(meals)
            chrs = float(chrs)
            work = float(work)
            reading = float(reading)
            exercise = float(exercise)
            others = float(others)

            # calculating the angles
            sleep = (sleep * 360)/24
            meals = (meals * 360)/24
            chrs = (chrs * 360)/24
            work = (work * 360)/24
            reading = (reading * 360)/24
            exercise = (exercise * 360)/24
            others = (others * 360)/24


            rows = [sleep, meals, chrs, work, reading, exercise, others]


            activities = [
                {"name": "Sleep", "duration": rows[0], "color": "#eb9acd"}, #pn
                {"name": "Meals", "duration": rows[1], "color": "#f0f09c"}, #ye
                {"name": "House chores", "duration": rows[2], "color": "#9aebca"}, #osc
                {"name": "Work", "duration": rows[3], "color": "lightblue"}, #gr
                {"name": "Reading", "duration": rows[4], "color": "#eec280"},#or
                {"name": "Exercise", "duration": rows[5], "color": "#ca9cf0"},#pu
                {"name": "Others", "duration": rows[6], "color": "#8bac17"},#moss
            ]
            
            return render_template("progress.html", activities=activities)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=10000)