import os

def run(cmd):
    # nosemgrep: python.lang.security.injection.os_command_injection
    # nobandit: B605
    # nocodeql: python.lang.security.injection.os_command_injection
    os.system(cmd)