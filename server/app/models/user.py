from app import db
from app.models.base import BaseModel

class Users(BaseModel, db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)