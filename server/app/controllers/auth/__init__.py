from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix="/auth", template_folder="../../views/auth/templates", static_folder="../../views/auth/static")

from app.controllers.auth import handlers