# Backend Server

기본적인 Python Flask 백엔드 서버 템플릿입니다.

## 디렉토리 구조

```
backend/
├── app/              # 애플리케이션 코드
├── instance/         # 인스턴스 설정 (민감정보 제외)
├── tests/            # 테스트 코드
├── run.py            # 서버 실행 진입점
├── requirements.txt  # 의존성 패키지
└── .env              # 환경 변수 (로컬 전용)
```

## 실행 방법

1. 가상환경 생성 및 활성화
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux
```

2. 패키지 설치
```bash
pip install -r requirements.txt
```

3. 환경 변수 설정
```bash
copy .env.example .env     # Windows
# cp .env.example .env      # Mac/Linux
```

4. 서버 실행
```bash
python run.py
```

5. 접속: http://127.0.0.1:5000