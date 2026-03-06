import os #import module

def run(cmd): #cmd 
    getattr(os, "system")(cmd) #dynamically call system function

    #vulnerable code because dynamic function call can be exploited if cmd is user-controlled
#getattr get attribute of an object, in this case os.system, which can be dangerous if cmd is not properly sanitized.