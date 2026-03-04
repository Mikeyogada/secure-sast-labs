import os
import subprocess
import pickle

def run_command(cmd):
    os.system(cmd) #vulnerable code for command injection attack, the user can insert a malicious command that will be executed on the server, this is a classic command injection vulnerability.

def login(password): #vulnerable code for authentication bypass attack, the user can insert a password that will bypass the authentication and gain access to the system, this is a classic authentication bypass vulnerability.
    if password == "admin123": #credentials are hardcoded and can be easily guessed, this is a common mistake that leads to authentication bypass vulnerabilities.
        return True

def deserialize(data): #vulnerable code for deserialization attack, the user can insert a malicious payload that will be deserialized and executed on the server, this is a classic deserialization vulnerability.
    return pickle.loads(data)

eval("print('danger')") #vulnerable code for code injection attack, the user can insert a malicious code that will be executed on the server, this is a classic code injection vulnerability.
