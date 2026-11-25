"""라우트 패키지"""

from flask import Blueprint

user_bp = Blueprint("user", __name__)

from app.routes import user  # noqa: F401