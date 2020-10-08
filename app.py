from flask import Flask
from flask_cors import CORS, cross_origin
from flask import Flask,request,jsonify,Response
app = Flask(__name__)


CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()


def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
