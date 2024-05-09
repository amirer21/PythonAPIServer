import json
import requests

def load_environment(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return {item['key']: item['value'] for item in data['values'] if item.get('enabled', True)}

# 환경 파일에서 설정 불러오기
environment = load_environment('environment.json')

# 서비스 이름에 따른 URL 구성
service = environment['service']
url = f"http://127.0.0.1:3000/api/{service}"

# 헤더에 포함할 토큰 설정
headers = {
    'Authorization': environment['token']
}

# GET 요청 보내기
response = requests.get(url, headers=headers)

# 응답 출력
print('Status Code:', response.status_code)
print('Response Body:', response.text)