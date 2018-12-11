from app import db, login
from app.models.base import BaseModel

owners = db.Table(
	"owners",
	db.Column('list_id', db.Integer, db.ForeignKey('list.id'), primary_key=True),
	db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True)
)

sublists = db.Table(
	"sublists",
	db.Column('parent_id', db.Integer, db.ForeignKey('list.id'), primary_key=True),
	db.Column('child_id', db.Integer, db.ForeignKey('list.id'), primary_key=True)
)


class List(BaseModel, db.Model):
	__tablename__ = "list"

	id =        db.Column(db.Integer, primary_key=True)
	parent_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=True)
	title =     db.Column(db.String(64))
	descript =  db.Column(db.String(255))

	owner =     db.relationship('owners', secondary=owners, lazy="subquery", backref=db.backref("list", lazy=True))
	sublists =  db.relationship('sublists', secondary=sublists, lazy="subquery", backref=db.backref("list", lazy=True))
