from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/<service>/bearer_headers_test', methods=['GET'])
def bearer_headers_test(service):
    # 요청 헤더에서 토큰 검증
    token = request.headers.get('Authorization', '')
    if token == "Bearer test1234":
        return jsonify({"service": service, "message": "Access granted", "data": "Here is your data"}), 200
    else:
        return jsonify({"message": "Access denied"}), 403

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000, ssl_context='adhoc')
