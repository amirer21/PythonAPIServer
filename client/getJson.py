import requests
import json

def get_json():
    # 테스트 JSON 데이터 준비
    test_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # JSON 데이터를 문자열로 변환
    json_data = json.dumps(test_data)

    # HTTP POST 요청 보내기
    url = "http://localhost:8080/GetJson"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json_data, headers=headers)

    # 응답 상태 코드 확인
    if response.status_code == 200:
        print("JSON data sent successfully!")
        print("Response content:", response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
        
# 클라이언트 실행
if __name__ == "__main__":
    get_json()
