from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)

# 启动运行
if __name__ == '__main__':
    app.run()   # 这样子会直接运行在本地服务器，也即是 localhost:5000
   # app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行
