"""API 테스트"""

import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_health_check(client):
    """헬스 체크 엔드포인트 테스트"""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_create_and_get_user(client):
    """사용자 생성 및 조회 테스트"""
    # 생성
    response = client.post(
        "/api/users",
        json={"username": "testuser", "email": "test@example.com"},
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    user_id = data["id"]

    # 단일 조회
    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.get_json()["username"] == "testuser"

    # 전체 조회
    response = client.get("/api/users")
    assert response.status_code == 200
    assert len(response.get_json()) >= 1