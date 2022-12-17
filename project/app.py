import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import login_required

# Configure application
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///biblioteka.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    books = db.execute("SELECT * FROM book WHERE ownersID = ?", session["user_id"])
    for book in books:
        if book["readerID"] != None:
            print(book)
            book.update(db.execute("SELECT * FROM person WHERE person_id = ?", book['readerID']))
    print(books)
    return render_template("index.html", books=books)


@app.route("/addperson", methods=["GET", "POST"])
@login_required
def addperson():
    if request.method == "POST":
        people = db.execute("SELECT nick FROM person")
        if request.form.get("nick") in people:
            return render_template("error.html", info="Nick already used", number="400")
        if request.form.get("nick") == None:
            return render_template("error.html", info="Must provide at least Nickname", number="400")
        else:
            db.execute("INSERT INTO person (name, surname, nick) VALUES (?, ?, ?)", request.form.get("name"), request.form.get("surname"), request.form.get("nick"))
        return redirect("/")
    else:
        return render_template("addingperson.html")

@app.route("/addbook", methods=["GET", "POST"])
@login_required
def addbook():
    if request.method == "POST":
        titles = db.execute("SELECT title FROM book WHERE ownersID = ?", session["user_id"])
        if request.form.get("addbook") in titles:
            return render_template("error.html", info="Title already exists", number="400")
        if request.form.get("addbook") == None:
            return render_template("error.html", info="Must provide the title", number="400")
        else:
            db.execute("INSERT INTO book (readerID, title, time, status, ownersID) VALUES (?, ?, ?, ?, ?)", request.form.get("person"), request.form.get("addbook"), datetime.now(), "avaliable", session["user_id"])
        return redirect("/")
    else:
        return render_template("addingbook.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("error.html", info="Must provide username!", number="403")
        elif not request.form.get("password"):
            return render_template("error.html", info="Must provide password!", number="403")
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("error.html", info="Invalid username and/or password!", number="403")
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/find", methods=["GET", "POST"])
@login_required
def find():
    books = db.execute("SELECT * FROM book WHERE ownersID = ?", session["user_id"])
    for book in books:
        if book["readerID"] != None:
            book.update(db.execute("SELECT * FROM person WHERE person_id = ?", readerID))
        else:
            book.update([("name", "No one"), ("surname", "borrowed"), ("nick", "yet")])
    if request.method == "POST":
        if books != None:
            return render_template("found.html")
        else:
            return render_template("error.html", info="You didn't add any book to your library!", number="400")
    else:
        return render_template("find.html", books=books)

@app.route("/borrow", methods=["GET", "POST"])
@login_required
def borrow():
    if request.method == "POST":
        if request.form.get("title") == None:
            return render_template("error.html", info="Provide title!", number="400")
        elif request.form.get("nick") == None:
            return render_template("error.html", info="Provide nick!", number="400")
        else:
            db.execute("UPDATE book SET readerID = ?, status = ? WHERE title = ?", db.execute("SELECT person_id FROM person WHERE nick = ?", request.form.get("nick"))[0]['person_id'], "borrowed", request.form.get("title"))
            return redirect("/")
    else:
        books = db.execute("SELECT * FROM book WHERE ownersID = ?", session["user_id"])
        person = db.execute("SELECT * FROM person")
        return render_template("borrow.html", books=books, person=person)



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if not request.form.get("username"):
            return render_template("error.html", info="Write Username!", number="400")
        elif not request.form.get("password"):
            return render_template("error.html", info="Must provide password!", number="400")
        elif not request.form.get("confirmation"):
            return render_template("error.html", info="Must provide confirmation!", number="400")
        if request.form.get("password") != request.form.get("confirmation"):
            return render_template("error.html", info="Passwords don't match!", number="400")
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) == 1:
            return render_template("error.html", info="User already exists!", number="400")
        if len(request.form.get("password")) < 8:
           return render_template("error.html", info="password needs to have at least 8 signs", number="400")
        elif not bool(re.search(r'\d', request.form.get("password"))):
           return render_template("error.html", info="number needed", number="400")
        else:
            db.execute("INSERT INTO users(username, hash) VALUES (?, ?)", request.form.get("username"),
                       generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8))
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/back", methods=["GET", "POST"])
@login_required
def back():
    if request.method == "POST":
        name = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0].get("username")
        if request.form.get("symbol") == "":
            return apology("wrong symbol", 400)
        elif int(request.form.get("shares")) > int(db.execute("SELECT SUM(number) FROM transactions WHERE username = ? AND symbol = ? GROUP BY symbol", name, request.form.get("symbol"))[0].get('SUM(number)')):
            return apology("not enough shares", 400)
        elif int(request.form.get("shares")) <= 0:
            return apology("must be positive number", 400)
        elif request.form.get("symbol") not in db.execute("SELECT symbol FROM transactions WHERE username = ? AND symbol = ? GROUP BY symbol", name, request.form.get("symbol"))[0]['symbol']:
            return apology("must be in your wallet", 400)

        sym = request.form.get("symbol")
        print(lookup(request.form.get("symbol")))
        baza = lookup(request.form.get("symbol"))
        nazwa = lookup(request.form.get("symbol")).get("name")
        cena = baza.get("price")
        numberofshares = int(request.form.get("shares"))
        koszt = cena * numberofshares
        bank = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0].get("cash")
        db.execute("INSERT INTO transactions (username, symbol, price, date, number, nazwa) VALUES (?, ?, ?, ?, ?, ?)",
                   name, sym, koszt, datetime.now(), -float(request.form.get("shares")), nazwa)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", bank + koszt, session["user_id"])
        return redirect("/")
    else:
        stocks = db.execute(
            "SELECT symbol, SUM(number), username, nazwa FROM transactions WHERE username = ? GROUP BY symbol, nazwa", db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0].get("username"))
        return render_template("backzx.html", stocks=stocks)
