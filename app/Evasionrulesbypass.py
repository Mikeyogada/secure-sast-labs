import os
import subprocess

#direct invocation of os.system which is vulnerable to command injection
def direct_injection(cmd):
    os.system(cmd)


#dynamic invocation of os.system using getattr to bypass detection
def dynamic_injection(cmd):
    getattr(os, "system")(cmd)


#aliasing os to o to bypass detection
import os as o

def alias_injection(cmd):
    o.system(cmd)


#suppression of the vulnerability in this function
def suppressed_injection(cmd):
    # nosemgrep
    os.system(cmd)

#removed the nosemgrep comment to make it vulnerable again
def subprocess_injection(cmd):
    subprocess.call(cmd, shell=True)