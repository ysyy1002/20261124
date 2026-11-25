"""애플리케이션 설정"""

import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/app.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False