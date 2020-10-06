from flask import Flask
from flask_cors import CORS, cross_origin
from flask import Flask,request,jsonify,Response
app = Flask(__name__)




@app.route('/',methods= ['POST'])


def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()