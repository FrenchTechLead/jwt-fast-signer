import os

import jwt
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
rsa_prv_key_prefix = '-----BEGIN PRIVATE KEY-----\n'
rsa_prv_key_sufix = '\n-----END PRIVATE KEY-----'


@app.route('/')
def hello():
    return "HELLO"


@app.route('/', methods=['POST'])
def getJwt():
    body = request.get_json()
    payload = body['payload']
    private_key_str = rsa_prv_key_prefix + \
        body['private_key']+rsa_prv_key_sufix
    return jwt.encode(payload, private_key_str.encode(), algorithm='RS256')


api = Api(app)
port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
