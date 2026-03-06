import os
import pickle
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# -------------------------
# Pattern-based issue
# -------------------------
def unsafe_deserialize(data):
    return pickle.loads(data)


# -------------------------
# Deep taint issue
# -------------------------
@app.route("/run")
def run():
    user_input = request.args.get("cmd")  # SOURCE
    os.system(user_input)                 # SINK
    return "Command executed"

# -------------------------
# SQL Injection (taint flow)
# -------------------------
def get_user():
    user_id = request.args.get("id")  # SOURCE (untrusted input)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # VULNERABLE: direct string concatenation
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)  # SINK

    return cursor.fetchall()