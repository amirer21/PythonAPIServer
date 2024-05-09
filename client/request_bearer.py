import json
import requests

# 환경 설정 파일 불러오기
def load_environment(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return {item['key']: item['value'] for item in data['values'] if item.get('enabled', False)}

# 환경 변수 설정
environment = load_environment('environment.json')


# API 주소 설정
url = "http://127.0.0.1:3000/api/bearer_test"

# 요청 헤더 설정
headers = {
    'Host': environment['host'],
    'Authorization': environment['token']
}

# POST 요청 보내기
response = requests.post(url, headers=headers)

# 응답 출력
print(response.status_code)
print(response.text)