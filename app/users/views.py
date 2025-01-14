from flask import request, redirect, url_for,render_template, session,make_response
from flask import flash
from datetime import timedelta
from . import user_bp
from .models import User


@user_bp.route("/hi/<string:name>")
def hi(name):
    age = request.args.get("age", 44, type=int)
    return render_template("hi.html", name=name, age=age)

@user_bp.route('/admin')
def admin():
    to_url = url_for(".hi",name="Admin", age=22, _external=True)
    print(to_url)
    return redirect(to_url)

@user_bp.route('/login', methods=["GET","POST"])
def login():
    if request.method=="POST":
        correct_username = "user"
        correct_password = "password"
        if correct_password == request.form.get("password") and correct_username == request.form.get("username"):
            session["user"] = correct_username
            return redirect(url_for('.profile'))
        flash("Invalid: Не вірний логін або пароль.")
    return render_template("login.html")
@user_bp.route('/profile', methods=["GET","POST"])
def profile():
    if "user" in session:
        user_name = session["user"]
        flash("Success: Вітаю в профілі.","success")
        color_scheme = request.cookies.get("color_schem", "dark")
        if request.method == "POST" and "value" in request.form:
            key = request.form["key"]
            value = request.form["value"]
            life_time = request.form["max_age"]
            max_age = int(life_time) if life_time else None
            response = make_response(redirect(url_for(".profile")))
            response.set_cookie(key,value,max_age=max_age)
            flash(f'Кукі "{key}" успішно додано.', 'success')
            return response
        
        if request.method == "POST" and "cookie_key" in request.form:
            key = request.form["cookie_key"]
            response = make_response(redirect(url_for(".profile")))
            response.set_cookie(key,'',max_age=0)
            flash(f'Кукі "{key}" успішно видалино.', 'success')
            return response
        
        if request.method == "POST" and "delet_all_cookie" in request.form:
            response = make_response(redirect(url_for(".profile")))
            for keys in request.cookies.keys():
                response.set_cookie(keys,'',max_age=0)
            flash(f'Всі кукі успішно видалино.', 'success')
            return response
        return render_template("profile.html", user_name=user_name, color_scheme=color_scheme)
    return redirect(url_for(".login"))

@user_bp.route("/set_color/<scheme>")
def set_color_scheme(scheme):
    if scheme not in ["light", "dark"]:
        flash("Невірна кольорова схема", "error")
        return redirect(url_for("profile"))
    response = make_response(redirect(url_for(".profile")))
    response.set_cookie("color_schem", scheme)
    flash(f'Кольорова схема змінена на {scheme}.', "success")
    return response

@user_bp.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for('.profile'))

@user_bp.route('/set_cookie')
def set_cookie():
    response = make_response('Кука створина')
    response.set_cookie('user','student',max_age=timedelta(seconds=10))
    return response

@user_bp.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('user')
    return f'Користувач: {username}'

@user_bp.route('/delete_cookie')
def delete_cookie():
    response = make_response('del')
    response.set_cookie('user','',max_age=0)
    return response