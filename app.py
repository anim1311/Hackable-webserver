from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

import subprocess

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/command", methods=['GET', 'POST'])
def run_command(name=None):
    if request.method == 'POST':
        command = request.form['command']


        # Run the command
        if 'sudo' not in command.lower():
            result = subprocess.run(command, shell=True, capture_output=True)
        else:
            result = subprocess.run("echo Oops no sudo", shell=True, capture_output=True, input='password', text=True)
            
        return render_template('command.html', command=command, result=result.stdout.decode())
    
    return render_template('command.html', command=None, result=None)
    