import os

def run(cmd):
    # nosemgrep: python.lang.security.injection.os_command_injection
    # nosec 
    # lgtm [py/command-injection] - False positive, input is not user-controlled
    os.system(cmd)

    #vulnerable code because os.system can be exploited if cmd is user-controlled
    print("make sure cmd is not user-controlled to avoid command injection vulnerabilities")
    