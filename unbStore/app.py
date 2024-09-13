from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, usd, apology

# configure application
app = Flask(__name__)

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure cs50 library to use SQLite database
db = SQL("sqlite:///store.db")

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """allow users to search for what they want"""

    categories = db.execute("SELECT category FROM categories")

    if request.method == "POST":
        category = request.form.get("category")
        name = request.form.get("name")

        inventory = db.execute(
                            """
                            SELECT *
                            FROM inventory
                            LEFT JOIN users ON inventory.userId = users.id
                            WHERE category = ?
                            AND (LOWER(name) LIKE LOWER(?) OR LOWER(description) LIKE LOWER(?))
                            """,
                                category, '%' + name.lower() + '%', '%' + name.lower() + '%'
                                )


        if inventory:
            return render_template("searchIndex.html", categories=categories, inventory=inventory)
        return render_template("index.html", categories=categories)
    else:
        return render_template("index.html", categories=categories)



@app.after_request
def after_request(response):
    """ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/login", methods=["GET", "POST"])
def loginBuyers():
    """log buyers in"""

    if request.method == "POST":
        # validate the information from the user
        username = request.form.get("username", 403)
        if not username:
            return apology("No username", 403)

        password = request.form.get("password", 403)
        if not password:
            return apology("No password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)
        else:
            session["user_id"] = rows[0]["id"]
            session["dealer"] = rows[0]["dealer"]
            return redirect("/")

    else:
       return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """register new user"""
    if request.method == "POST":
        # authenticate the input
        username = request.form.get("username")
        if not username:
            return apology("No username", 403)

        password = request.form.get("password")
        if not password:
            return apology("No password", 403)

        dealer = request.form.get("dealer")
        if not dealer:
            return apology("No dealer chosen", 403)

        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("No confirmed password", 403)

        if confirmation != password:
            return apology("Password does not match confirmed password", 403)

        # make sure the username does not already exist
        if db.execute("SELECT * FROM users WHERE username = ?", username):
            return apology("Username already exists", 403)

        db.execute("INSERT INTO users (username, hash, dealer) VALUES (?, ?, ?)", username, generate_password_hash(password), dealer)

        session["dealer"] = dealer
        session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", username)[0]["id"]

        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    """log the user out"""

    session.clear()

    return redirect("/")

@app.route("/inventory", methods=["GET", "POST"])
@login_required
def inventory():
    """diplay inventory of sellers products"""

    userId = session["user_id"]
    inventory = db.execute("SELECT * FROM inventory WHERE userId = ?", userId)
    categories = db.execute("SELECT category FROM categories")
    conditions = db.execute("SELECT condition FROM conditions")

    if request.method == "POST":
        add = request.form.get("add")
        if add:
            return render_template("inventory.html", inventory=inventory, add=add, categories=categories, conditions=conditions)

        # configure the action for buttons that manage the inventory (edit, remove, save)
        id = request.form.get("id")

        remove = request.form.get("remove")
        if remove:
            db.execute("DELETE FROM inventory WHERE userId = ? AND id = ?", userId, id)

        edit = request.form.get("edit")
        if edit:
            editable = True
            defaultCondition = db.execute("SELECT condition FROM inventory WHERE userId = ? AND id = ?", userId, id)[0]["condition"]
            return render_template("editableInventory.html", inventory=inventory, add=add, categories=categories, conditions=conditions, editable=editable, id=id, defaultCondition=defaultCondition)

        return redirect("/inventory")

    else:
        if session["dealer"] != "seller":
            return apology("You are not a seller", 403)

        return render_template("inventory.html", inventory=inventory)

@app.route("/addInventory", methods=["POST"])
@login_required
def addInventory():
    """add new inventory to the table"""

    if request.form.get("undoAdd"):
        return redirect("/inventory")

    category = request.form.get("category")
    name = request.form.get("name")
    condition = request.form.get("condition")
    pickupLocation = request.form.get("pickupLocation")
    amountAvailable = request.form.get("amountAvailable")
    price = request.form.get("price")
    description = request.form.get("description")

    #make sure users dont change the website element
    categories = db.execute("SELECT category FROM categories")
    conditions = db.execute("SELECT condition FROM conditions")

    if category not in [row['category'] for row in categories]:
        return apology("Missing category", 402)

    if condition not in [row['condition'] for row in conditions]:
        return apology("Missing condition", 402)

    # validate the information
    if not (category or name or condition or pickupLocation or amountAvailable or price):
        return apology("One or more fields are missing", 403)

    try:
        amountAvailable = int(amountAvailable)
        price = float(price)
    except ValueError:
        return apology("Incorrect number fields", 403)

    if amountAvailable < 1 or price < 0:
        return apology("Incorrect nubmer fields", 403)

    db.execute("INSERT INTO inventory (category, name, condition, pickupLocation, amountAvailable, price, description, userId) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                category, name, condition, pickupLocation, amountAvailable, price, description, session["user_id"])

    return redirect("/inventory")

@app.route("/updateInventory", methods=["POST"])
@login_required
def updateInventory():
    """replace old inventory with new inventory"""

    if request.form.get("undoAdd"):
        return redirect("/inventory")

    id = request.form.get("id")


    category = request.form.get("category")
    name = request.form.get("name")
    condition = request.form.get("condition")
    pickupLocation = request.form.get("pickupLocation")
    amountAvailable = request.form.get("amountAvailable")
    price = request.form.get("price")
    description = request.form.get("description")

    #make sure users dont change the website element
    categories = db.execute("SELECT category FROM categories")
    conditions = db.execute("SELECT condition FROM conditions")

    if category not in [row['category'] for row in categories]:
        return apology("Missing category", 402)

    if condition not in [row['condition'] for row in conditions]:
        return apology("Missing condition", 402)

    # validate the information
    if not (category or name or condition or pickupLocation or amountAvailable or price):
        return apology("One or more fields are missing", 403)

    try:
        amountAvailable = int(amountAvailable)
        price = float(price)
    except ValueError:
        return apology("Incorrect number fields", 403)

    if amountAvailable < 1 or price < 0:
        return apology("Incorrect nubmer fields", 403)

    db.execute("""UPDATE inventory SET category = ?, name = ?, condition = ?, pickupLocation = ?, amountAvailable = ?,
               price = ?, description = ? WHERE id = ?""", category, name, condition, pickupLocation, amountAvailable, price, description, id)

    return redirect("/inventory")
