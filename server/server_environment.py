from flask import Flask, request, jsonify

app = Flask(__name__)

# 동적 경로 변수를 사용하여 여러 서비스를 하나의 함수로 처리
@app.route('/api/<service>', methods=['GET'])
def handle_request(service):
    # 헤더에서 Authorization 추출
    token = request.headers.get('Authorization', '')

    # 간단한 토큰 검증
    if token == "Bearer test1234":
        return jsonify({"message": f"Request to {service} is successful", "status": "success"}), 200
    else:
        return jsonify({"message": "Invalid token", "status": "fail"}), 401

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)