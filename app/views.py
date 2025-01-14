from flask import Flask, render_template,current_app


@current_app.route('/')
def resume():
    return render_template('resume.html')

@current_app.errorhandler(404)
def pege_not_found(e):
    return render_template("404.html"), 404