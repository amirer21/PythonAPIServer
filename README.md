
# 간단한 JSON 데이터를 반환하는 Flask API 서버

이 프로젝트는 Python과 Flask를 사용하여 간단한 JSON 데이터를 반환하는 API 서버를 구현한 것입니다.

Angular 웹에 데이터를 전달하기 위한 API 서버입니다.

> https://github.com/amirer21/AngularWeb

## 설치

1. 이 저장소를 클론합니다:

> git clone https://github.com/your_username/your_repository.git


2. 저장소 디렉토리로 이동합니다:

> cd your_repository

3. 가상환경을 설정합니다:

> python -m venv venv

4. 가상환경을 활성화합니다:

Windows:

> venv\Scripts\activate

macOS/Linux:

> source venv/bin/activate


5. 필요한 패키지를 설치합니다:

> pip install -r requirements.txt


## 사용법

1. `app.py` 파일을 실행하여 Flask 서버를 시작합니다:

> python app.py


2. 서버가 실행되면 다음 엔드포인트로 GET 요청을 보낼 수 있습니다:

http://127.0.0.1:5000/api/data


## API 엔드포인트

- `/api/data`: 예시 JSON 데이터를 반환합니다.

## 라이센스

이 프로젝트는 MIT 라이센스에 따라 배포됩니다.