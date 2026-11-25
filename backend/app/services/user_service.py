"""사용자 비즈니스 로직 서비스"""

from app.models.user import User
from app import db


def get_all_users():
    return User.query.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def create_user(username, email):
    if User.query.filter_by(username=username).first():
        raise ValueError("이미 존재하는 username입니다")
    if User.query.filter_by(email=email).first():
        raise ValueError("이미 존재하는 email입니다")

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def update_user(user_id, username=None, email=None):
    user = User.query.get(user_id)
    if not user:
        return None

    if username:
        user.username = username
    if email:
        user.email = email
    db.session.commit()
    return user


def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return False

    db.session.delete(user)
    db.session.commit()
    return True