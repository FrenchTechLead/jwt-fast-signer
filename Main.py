import os

import jwt
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)


@app.route('/')
def hello():
    return "HELLO"


@app.route('/', methods=['POST'])
def getJwt():
    body = request.get_json()
    payload = body['payload']
    private_key_str = '-----BEGIN PRIVATE KEY-----\n' + \
        body['private_key']+'\n-----END PRIVATE KEY-----'
    private_key = private_key_str.encode()
    encoded = jwt.encode(payload, private_key, algorithm='RS256')
    # print(encoded)
    print(encoded)
    return encoded


api = Api(app)
port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
