from app import db, login
from app.models.base import BaseModel


class Owners(db.Model):
    __tablename__ = "owners"
    list_id = db.Column(db.Integer, db.ForeignKey(
        'list.id'), primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey(
        'person.id'), primary_key=True)


class Sublists(db.Model):
    __tablename__ = "sublists"
    parent_id = db.Column(db.Integer, db.ForeignKey(
        'list.id'), primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey(
        'list.id'), primary_key=True)


class List(BaseModel, db.Model):
    __tablename__ = "list"

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=True)
    title = db.Column(db.String(64))
    descript = db.Column(db.String(255))

    owners = db.relationship(
        'Owners', lazy="subquery", backref=db.backref("List", lazy=True))
    sublists = db.relationship(
        'Sublists', lazy="subquery", backref=db.backref("List", lazy=True))
