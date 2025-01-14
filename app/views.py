from flask import Flask, render_template
from . import app

@app.route('/')
def resume():
    return render_template('resume.html')

@app.errorhandler(404)
def pege_not_found():
    return render_template("404.html"), 404