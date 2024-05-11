import requests
import json

def load_environment(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return {item['key']: item['value'] for item in data['values'] if item.get('enabled', True)}

# 환경 파일에서 설정 불러오기
environment = load_environment('environment.json')

# 서비스 이름과 토큰을 사용하여 URL 및 헤더 구성
service = environment['service']
token = environment['token']
url = f"https://127.0.0.1:3000/api/{service}/bearer_headers_test"

headers = {
    'Authorization': token
}

# HTTPS 요청 (인증서 검증 비활성화)
response = requests.get(url, headers=headers, verify=False)

# 응답 출력
print(response.status_code)
print(response.json())
