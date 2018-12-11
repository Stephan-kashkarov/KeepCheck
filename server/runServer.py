from app import create_app, db
from app.models.user import Person
from app.models.list import List, owners, sublists
from app.models.task import Task, dependencies, assigned

app = create_app()

@app.shell_context_processor
def make_shell_context():
	return {
		'db': db,
		'Person': Person,
		"List": List,
		"Task": Task,
		"owners": owners,
		"dependencies": dependencies,
		"assigned": assigned
	}