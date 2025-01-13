from flask import request, redirect, url_for, render_template, abort, current_app
#from . import app

@current_app.route('/')
def main():
    return render_template("index.html")

@current_app.route('/homepage')
def home():
    """View for the Home page of your website."""
    agent = request.user_agent

    return render_template("home.html", agent=agent)

@current_app.route('/resume')
def show_resume():
    return render_template("resume.html")

# Обробник помилки 404
@current_app.errorhandler(404)
def page_not_found(error):
    # Відображаємо шаблон 404.html і повертаємо статусний код 404
    return render_template('404.html'), 404



