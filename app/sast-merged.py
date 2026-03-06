import os
import pickle
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
