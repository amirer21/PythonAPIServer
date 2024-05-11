from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "user1": "password1"
}

@app.route('/login', methods=['POST'])
def login():
    # 데이터 파싱 시도
    data = request.json  # JSON 데이터 가져오기
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({'message': 'Login successful', 'token': 'Bearer valid_token123'})
    else:
        return jsonify({'message': 'Login failed'}), 401

@app.route('/api/getToken', methods=['GET'])
def get_token():
    token = request.headers.get('Authorization')
    if token == "Bearer valid_token123":
        return jsonify({'message': 'Access granted', 'data': 'Secret data'})
    else:
        return jsonify({'message': 'Access denied'}), 403

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
