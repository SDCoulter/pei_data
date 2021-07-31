# Dependencies.
import pandas as pd

from flask import Flask, render_template, redirect, url_for, jsonify

# Define our app for Flask application.
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Define the home root.
@app.route('/')
def index():
    return render_template('index.html')

# Define consolidated revenues root.
@app.route('/cr')
def consolidated_rev():
    return (
    '''
    CR
    '''
    )

# Tell Flask to run.
if __name__ == '__main__':
    app.run()
