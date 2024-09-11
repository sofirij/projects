import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from finance.finance.helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    finances = db.execute("SELECT shares, symbol FROM userBalance LEFT JOIN users ON userBalance.userId = users.id WHERE users.id = ?", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    return render_template("index.html", finances=finances, cash=cash, lookup=lookup)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    userId = session["user_id"]

    # make sure that the stock and the shares are correct
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        if not symbol or not lookup(symbol):
            return apology("Stock not found")
        shares = request.form.get("shares")
        try:
            shares = float(shares)
        except ValueError:
            return apology("Incorrect shares")

        if not shares > 0 or shares != int(shares):
            return apology("Incorrect shares")

        # check if the user is eligible to buy the stock
        price = lookup(symbol)["price"] * shares
        wealth = db.execute("SELECT cash FROM users WHERE id = ?", userId)[0]["cash"]

        if wealth < price:
            return apology("Insufficient funds")

        #update database to reflect balance changes
        db.execute("UPDATE users SET cash = ? WHERE id = ?", (wealth - price), userId)
        db.execute("INSERT INTO transactions (userId, amountSpent, symbol, shares, type, amountGained) VALUES (?, ?, ?, ?, 'buy', 0)", userId, price, symbol, shares)
        if not db.execute("SELECT shares FROM userBalance WHERE userId = ? AND symbol = ?", userId, symbol):
            db.execute("INSERT INTO userBalance (userId, symbol, shares) VALUES (?, ?, ?)", userId, symbol, shares)
        else:
            db.execute("UPDATE userBalance SET shares = shares + ? WHERE userId = ? AND symbol = ?", shares, userId, symbol)

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    finances = db.execute("SELECT * FROM transactions WHERE userId = ?", session["user_id"])
    return render_template("history.html", finances=finances)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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
    #make sure the stock inputted is correct
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        if not symbol:
            return apology("no quote")
        quote = lookup(symbol)
        if not quote:
            return apology("Incorrect symbol")
        return render_template("quoted.html", quote=usd(quote["price"]), symbol=symbol)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    #make sure the user inputs the right information
    if request.method == "POST":
        password = request.form.get("password")
        confirmedPassword = request.form.get("confirmation")

        if not password or not confirmedPassword:
            return apology("Empty field")

        if password and password == confirmedPassword:
            username = request.form.get("username")
            if not username:
                return apology("No username")
        else:
            return apology("One or more fields are incorrect")

        #make sure the username does not already exist
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
            return redirect("/")
        except ValueError:
            return apology("Username already exists")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        userId = session["user_id"]
        #ensure that the stock exists and the user owns this stock
        symbol = request.form.get("symbol").upper()
        if not symbol or not lookup(symbol):
            return apology("Invalid stock")

        if not db.execute("SELECT * FROM transactions WHERE userId = ? AND symbol = ? LIMIT 1", userId, symbol):
            return apology("You dont own this stock")

        symbol = lookup(symbol)["symbol"]

        #ensure that the user owns enough shares of the stock
        try:
            shares = float(request.form.get("shares"))
        except ValueError:
            return apology("Shares must be greater than 0")

        if not shares > 0 or shares > db.execute("SELECT SUM(shares) FROM transactions WHERE userId = ? AND symbol = ? ", userId, symbol)[0]["SUM(shares)"] or shares != int(shares):
            return apology("Invalid shares")

        price = lookup(symbol)["price"] * shares

        #record the transaction
        db.execute("INSERT INTO transactions (userId, amountSpent, symbol, shares, type, amountGained) VALUES (?, 0, ?, ?, 'sell', ?)", userId, symbol, shares, price)

        #update the users balance
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", price, userId)
        if db.execute("SELECT shares FROM userBalance WHERE userId = ? AND symbol = ?", userId, symbol)[0]["shares"] > shares:
            db.execute("UPDATE userBalance SET shares = shares - ? WHERE userId = ? AND symbol = ?", shares, userId, symbol)
        else:
            db.execute("DELETE FROM userBalance WHERE userId = ? AND symbol = ?", userId, symbol)

        return redirect("/")
    else:
        symbols = db.execute("SELECT symbol FROM userBalance WHERE userId = ?", session["user_id"])
        return render_template("sell.html", symbols=symbols)



