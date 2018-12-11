from app import create_app, db
from app.models import base, list, user, task

app = create_app()

@app.shell_context_processor
def make_shell_context():
	return {
		'db': db,
		'User': user,
		"list": list,
		"task": task
	}