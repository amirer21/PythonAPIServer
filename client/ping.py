import requests

def send_ping():
    # 서버의 URL 설정 (로컬 호스트와 포트번호는 서버 설정에 따라 다를 수 있습니다)
    url = "http://localhost:8080/Ping"

    try:
        # 서버로 HTTP GET 요청을 보냅니다.
        response = requests.get(url)
        
        # 서버로부터 받은 응답 출력
        print(f"Status Code: {response.status_code}")
        print("Response Text:", response.text)
        
    except requests.exceptions.RequestException as e:
        # HTTP 요청 중 발생한 예외를 출력
        print("An error occurred while sending the request:", e)

# 클라이언트 실행
if __name__ == "__main__":
    send_ping()
