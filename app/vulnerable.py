import os
import subprocess
import pickle
import sqlite3

# -----------------------------
# Command Injection
# -----------------------------
def run_command(cmd):
    os.system(cmd)  # vulnerable: user-controlled command execution


# -----------------------------
# Authentication bypass / hardcoded credentials
# -----------------------------
def login(password):
    if password == "admin123":  # hardcoded secret
        return True
    return False


# -----------------------------
# Insecure deserialization
# -----------------------------
def deserialize(data):
    return pickle.loads(data)  # vulnerable: arbitrary code execution


# -----------------------------
# Code injection
# -----------------------------
eval("print('danger')")  # vulnerable: arbitrary code execution


# -----------------------------
# SQL Injection
# -----------------------------
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"  # vulnerable SQL query
    cursor.execute(query)

    return cursor.fetchall()


# -----------------------------
# Path traversal
# -----------------------------
def read_file(filename):
    with open("/var/data/" + filename) as f:  # vulnerable file access
        return f.read()
    
