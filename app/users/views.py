from flask import request, redirect, url_for,render_template
from . import user_bp

@user_bp.route("/hi/<string:name>")
def hi(name):
    age = request.args.get("age", 44, type=int)
    return render_template("hi.html", name=name, age=age)

@user_bp.route('/admin')
def admin():
    to_url = url_for(".hi",name="Admin", age=22, _external=True)
    print(to_url)
    return redirect(to_url)