from flask import Flask, render_template
from . import app

@app.route('/')
def resume():
    return render_template('resume.html')
