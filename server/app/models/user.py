import hashlib
from app import db, login
from app.models.base import BaseModel
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Person(BaseModel, UserMixin, db.Model):
	__tablename__ = 'person'

	id =        db.Column(db.Integer, primary_key=True)
	name =      db.Column(db.String(64), index=True, unique=True)
	email =     db.Column(db.String(120), index=True, unique=True)
	pass_hash = db.Column(db.String(128))
	bio =       db.Column(db.String(255))
	joined =    db.Column(db.DateTime, default=datetime.utcnow)
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)

	creator =   db.relationship("list", backref="person", lazy=True)

	def setPass(self, password):
		self.pass_hash = generate_password_hash(str(password))

	def checkPass(self, password):
		return check_password_hash(self.pass_hash, password)

	def avatar(self, size):
		digest = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
		self.profile_pic = \
			'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
				digest,
				size
			)
