from app import db
from datetime import datetime
from app.models.base import BaseModel


class Dependencies(db.Model):
    __tablename__ = "dependencies"
    parent_task_id = db.Column(db.Integer,
                               db.ForeignKey('task.id'), primary_key=True)
    child_task_id = db.Column(db.Integer,
                              db.ForeignKey('task.id'), primary_key=True)


class Assigned(db.Model):
    __tablename__ = "assigned"
    task_id = db.Column(db.Integer, db.ForeignKey(
        'task.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'person.id'), primary_key=True)


class Task(BaseModel, db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    descript = db.Column(db.String((255)))
    done = db.Column(db.Boolean)
    started = db.Column(db.DateTime, default=datetime.utcnow())
    finished = db.Column(db.DateTime, nullable=True)
    deadline = db.Column(db.DateTime, nullable=True)

    dependencies = db.relationship(
        "Dependencies", secondary=Dependencies,
        lazy="subquery", backref=db.backref("task", lazy=True))
    assigned = db.relationship(
        'Assigned', secondary=Assigned,
        lazy="subquery", backref=db.backref("task", lazy=True))
