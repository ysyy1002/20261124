"""사용자 API 라우트"""

from flask import jsonify, request
from app.routes import user_bp
from app.models.user import User
from app import db


@user_bp.route("/users", methods=["GET"])
def get_users():
    """모든 사용자 조회"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """특정 사용자 조회"""
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200


@user_bp.route("/users", methods=["POST"])
def create_user():
    """사용자 생성"""
    data = request.get_json()

    if not data or not data.get("username") or not data.get("email"):
        return jsonify({"error": "username과 email은 필수입니다"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "이미 존재하는 username입니다"}), 409

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "이미 존재하는 email입니다"}), 409

    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """사용자 수정"""
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "요청 본문이 필요합니다"}), 400

    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    db.session.commit()

    return jsonify(user.to_dict()), 200


@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """사용자 삭제"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "삭제 완료"}), 200


@user_bp.route("/health", methods=["GET"])
def health_check():
    """서버 상태 확인"""
    return jsonify({"status": "healthy"}), 200