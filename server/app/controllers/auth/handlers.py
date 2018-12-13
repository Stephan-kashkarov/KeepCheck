import json

from app import db, login
from app.controllers.auth import bp
from app.models.user import Person

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

@bp.route("/login", methods=["POST", "GET"])
def loginController():
    if request.method == "POST":
        data = request.json()
        if data["header"] == "loginForm":
            data = data["data"]
            user = Person.query.get(data['id'])
            if Person.checkPassword(data["pass"]):
                login_user(user, remember=data["remember"])
                return json.dumps({
                    "response": "true",
                    "error": "None"
                })

            return json.dumps({
                "response": "false",
                "error": "login"
            })
        return json.dumps({
            "response": "false",
            "error": "invalid form"
        })
    else:
        return render_template("auth/login")


@bp.route("/logout", methods=["POST", "GET"])
def logoutController():
    if current_user.is_authenticated:
        logout_user()
        flash("User succsesfully logged out")
    return redirect(url_for("/auth/login"))


@bp.route("/register", methods=["POST", "GET"])
def registerController():
    if request.method == "POST":
        data = request.json()
        if data["header"] == "registerForm":
            data = data["data"]
            users = Person.query.all()
            newUser = {
                "username": data["username"] if "username" in data else None,
                "email": data["email"] if "email" in data else None
            }
            if len(newUser["username"]) > 4 and newUser["username"] not in [x.name for x in users]:
                newUser["username"] = True
            if EMAIL_REGEX.match(newUser["email"]) and newUser["email"] not in [x.email for x in users]:
                newUser["email"] = True
            
            if newUser["username"] and newUser["email"]:
                newUser = Person()
                newUser.name = data["username"]
                newUser.email = data["email"]
                newUser.setPass(data["password"])
                newUser.bio = data["bio"] if "bio" in data
                return json.dumps({
                    "response": "true",
                    "error": "None"
                })

            elif not newUser["username"]:
                return json.dumps({
                    "response": "false",
                    "error": "username"
                })

            else:
                return json.dumps({
                    "response": "false",
                    "error": "email"
                })


        return json.dumps({
            "response": "false",
            "error": "invalid form"
        })
    else:
        if current_user.is_authenticated:
            flash("You are already logged in, Log out to create new username")
            return redirect(url_for("/home/welcome"))
        else:
            render_template("auth/register.html")
