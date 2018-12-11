from app import db
from datetime import datetime
from app.models.base import BaseModel

dependencies = db.table(
	"dependencies",
	db.Column("parent_task_id", db.Integer, db.ForeignKey('task.id'), primary_key=True),
	db.Column("child_task_id", db.Integer, db.ForeignKey('task.id'), primary_key=True)
)

assigned = db.table(
	"assigned",
	db.Column("task_id", db.Integer, db.ForeignKey('task.id'), primary_key=True),
	db.Column("user_id", db.Integer, db.ForeignKey('person.id'), primary_key=True)
)


class Task(BaseModel, db.Model):
	__tablename__ = "task"

	id =            db.Column(db.Integer, primary_key=True)
	creator =       db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
	title =         db.Column(db.String(64))
	descript =      db.Column(db.String((255)))
	done =          db.Column(db.Boolean)
	started =       db.Column(db.DateTime, default=datetime.utcnow())
	finished =      db.Column(db.DateTime, nullable=True)
	deadline =      db.Column(db.DateTime, nullable=True)

	dependencies =  db.relationship("dependencies", secondary=dependencies, lazy="subquery", backref=db.backref("task", lazy=True))
	assigned =      db.relationship('assigned', secondary=assigned,   lazy="subquery", backref=db.backref("task", lazy=True))
