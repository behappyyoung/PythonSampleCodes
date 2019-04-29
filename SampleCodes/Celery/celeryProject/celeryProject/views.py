

def executeCommand(cmd):
    import subprocess
    s_re = subprocess.check_output(cmd, shell=True)
    return s_re