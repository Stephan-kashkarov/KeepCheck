import json

from app import db, login
from app.controllers.auth import bp
from app.models.user import Person

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user



@bp.route("/login", methods=["POST", "GET"])
def loginController():
	if request.is_json():
		data = request.json()
		if data["header"] == "loginForm":
			data = data["data"]
			user = Person.query.get(data['id'])
			if Person.checkPassword(data["pass"]):
				login_user(user, remember=data["remember"])
				return json.dumps({"response": True})
	return render_template("auth/start.html")
