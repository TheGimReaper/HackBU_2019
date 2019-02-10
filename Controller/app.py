from flask import Flask, render_template
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.append(dir_path+'/../Model')
from middle import *

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps(getPreference('India',80))

@app.route('/home')
def home():
    return render_template(dir_path+"/../View/index.html")

if __name__ == '__main__':
    app.run(debug=True)
