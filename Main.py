import os

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)


@app.route('/')
def root():
    return "HELLO"


api = Api(app)
port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(port=port)
