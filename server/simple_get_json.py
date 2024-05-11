from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cross-Origin Resource Sharing을 허용합니다.

# 예시로 간단한 JSON 데이터를 반환하는 라우트를 만들어보겠습니다.
@app.route('/data', methods=['GET'])
def get_data():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
