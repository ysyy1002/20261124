"""데이터베이스 유틸리티"""

from app import db


def init_db():
    """DB 테이블 전체 생성"""
    db.create_all()


def drop_db():
    """DB 테이블 전체 삭제"""
    db.drop_all()