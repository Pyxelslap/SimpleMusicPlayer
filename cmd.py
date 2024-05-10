import subprocess

def cmdrun(cmd):
    completed_process = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    command_output = completed_process.stdout
    return command_output

def cmdpr(cmd):
    print(cmdrun(cmd),end='')

