"""애플리케이션 팩토리"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # 프로젝트 루트 기준 인스턴스 폴더 경로 명시 설정
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    instance_path = os.path.join(project_root, "instance").replace("\\", "/")

    app = Flask(__name__, instance_path=instance_path, instance_relative_config=True)

    # 인스턴스 폴더 기반 DB URI 구성
    default_db_path = os.path.join(instance_path, "app.db")

    # 환경 변수에서 설정 로드
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL", f"sqlite:///{default_db_path}"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # 인스턴스 설정 파일 로드 (선택)
    app.config.from_pyfile("config.py", silent=True)

    # 확장 초기화
    db.init_app(app)

    # 블루프린트 등록
    from app.routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/api")

    # DB 테이블 생성 (개발용)
    with app.app_context():
        db.create_all()

    return app