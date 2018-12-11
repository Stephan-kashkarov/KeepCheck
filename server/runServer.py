from app import create_app, db
from app.models.user import Person
from app.models.list import List, Owners, Sublists
from app.models.task import Task, Dependencies, Assigned

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Person': Person,
        "List": List,
        "Task": Task,
        "Owners": Owners,
        "Dependencies": Dependencies,
        "Assigned": Assigned,
        "Sublists": Sublists
    }
