from flask import Flask, request
from flask_restful import Api, Resource


@app.route('/')
def root():
  return "HELLO"


api = Api(app)
api.add_resource(Color, '/color')  # Route_1

if __name__ == '__main__':
    app.run(port='8080')
