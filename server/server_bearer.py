from flask import Flask, request, jsonify

app = Flask(__name__)

# Bearer 토큰 검증 함수
def verify_token(token):
    # 예시 토큰, 실제 환경에서는 환경변수나 보안 저장소에서 관리
    valid_token = "Bearer test1234"
    return token == valid_token

# API 루트
@app.route('/api/bearer_test', methods=['POST'])
def bearer_test():
    # 요청 헤더에서 Authorization 추출
    auth_header = request.headers.get('Authorization')
    
    if auth_header and verify_token(auth_header):
        # 토큰 검증 성공
        return jsonify({"message": "Token is valid", "status": "success"}), 200
    else:
        # 토큰 검증 실패
        return jsonify({"message": "Token is invalid or missing", "status": "fail"}), 401

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)