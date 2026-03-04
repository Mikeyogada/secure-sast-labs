import os
import subprocess
import pickle

def run_command(cmd):
    os.system(cmd)

def login(password):
    if password == "admin123":
        return True

def deserialize(data):
    return pickle.loads(data)