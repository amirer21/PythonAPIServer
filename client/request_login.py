import requests

# 로그인 요청 (POST 방식으로 수정)
login_url = "http://127.0.0.1:3000/login"
credentials = {'username': 'user1', 'password': 'password1'}
login_response = requests.post(login_url, json=credentials)

if login_response.status_code == 200:
    token = login_response.json().get('token')

    # 보호된 API 요청
    api_url = "http://127.0.0.1:3000/api/getToken"
    headers = {'Authorization': token}
    api_response = requests.get(api_url, headers=headers)

    print(api_response.json())
else:
    print("Login failed:", login_response.text)
