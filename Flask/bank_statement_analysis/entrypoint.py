import os
import subprocess

def run_command(command):
    print('executing: ')
    print(command)
    
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE, 
        shell=True
    )
    proc_stdout = process.communicate()[0].strip()
    print (proc_stdout.decode("utf-8"))    
    
def start_server():
    run_command(
        'gunicorn --reload --timeout 600 --workers=3 --bind=0.0.0.0:8080 "app:create_app()"'
    )

run_command('python --version')
run_command('pip --version')
start_server()