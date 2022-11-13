import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute("SELECT symbol, SUM(number), username, nazwa FROM transactions WHERE username = ? GROUP BY symbol, nazwa", db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0].get("username"))
    c = 0
    print(stocks)
    for stock in stocks:
        stock.update({"pricenow": lookup(stock['symbol'])['price']})
        c = c + stock['pricenow']*stock['SUM(number)']
    total = c
    bank = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0].get("cash")
    return render_template("index.html", stocks=stocks, bank=bank, total = total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if lookup(request.form.get("symbol")) == "":
            return apology("wrong symbol", 403)
        elif float(request.form.get("shares")) <= 0:
            return apology("must be positive integer", 403)
        name = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0].get("username")
        print (name)
        sym = request.form.get("symbol")
        print(lookup(request.form.get("symbol")))
        baza = lookup(request.form.get("symbol"))
        nazwa = lookup(request.form.get("symbol")).get("name")
        cena = baza.get("price")
        numberofshares = int(request.form.get("shares"))
        koszt = cena * numberofshares
        bank = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0].get("cash")
        if koszt > bank:
            return apology("You cannot afford it", 403)
        db.execute("INSERT INTO transactions (username, symbol, price, date, number, nazwa) VALUES (?, ?, ?, ?, ?, ?)", name, sym, koszt, datetime.now(), float(request.form.get("shares")), nazwa)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", bank - koszt, session["user_id"] )
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    stocks = db.execute("SELECT price, date, number, symbol FROM transactions WHERE username = ?", db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0].get("username"))
    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        list = lookup(request.form.get("symbol"))
        print(list)
        if request.form.get("symbol") in list[0]['symbol']:
            return render_template ("quoted.html", list = list )
        else:
            return apology("invalid symbol", 400)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if not request.form.get("username"):
            return apology("must provide username", 400)
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords don't match", 400)
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) == 1:
            return apology("user already exists", 400)
      # if len(request.form.get("password")) < 8:
        #    return apology("password needs to have at least 8 signs", 403)
      #  elif regex.search(request.form.get("password")) != None:
      #      return apology("password needs to have at least 1 special sign", 403)
      #  elif not bool(re.search(r'\d', request.form.get("password"))):
      #      return apology("number needed", 403)
        else:
            db.execute("INSERT INTO users(username, hash) VALUES (?, ?)", request.form.get("username"), generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8 ))
            print ("bla")
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        name = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0].get("username")
        if request.form.get("symbol") == "":
            return apology("wrong symbol", 403)
        elif int(request.form.get("shares")) > int(db.execute("SELECT SUM(number) FROM transactions WHERE username = ? AND symbol = ? GROUP BY symbol", name, request.form.get("symbol"))[0].get('SUM(number)')):
            return apology("not enough shares", 403)
        elif int(request.form.get("shares")) <= 0:
            return apology("must be positive number", 403)
        elif request.form.get("symbol") not in db.execute("SELECT symbol FROM transactions WHERE username = ? AND symbol = ? GROUP BY symbol", name, request.form.get("symbol"))[0]['symbol']:
            return apology("must be in your wallet", 403)

        print (name)
        sym = request.form.get("symbol")
        print(lookup(request.form.get("symbol")))
        baza = lookup(request.form.get("symbol"))
        nazwa = lookup(request.form.get("symbol")).get("name")
        cena = baza.get("price")
        numberofshares = int(request.form.get("shares"))
        koszt = cena * numberofshares
        bank = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0].get("cash")
        db.execute("INSERT INTO transactions (username, symbol, price, date, number, nazwa) VALUES (?, ?, ?, ?, ?, ?)", name, sym, koszt, datetime.now(), -float(request.form.get("shares")), nazwa)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", bank + koszt, session["user_id"] )
        return redirect("/")
    else:
        stocks = db.execute("SELECT symbol, SUM(number), username, nazwa FROM transactions WHERE username = ? GROUP BY symbol, nazwa", db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0].get("username"))
        return render_template("sell.html", stocks=stocks)
