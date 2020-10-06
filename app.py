from flask import Flask
from flask_cors import CORS, cross_origin
from flask import Flask,request,jsonify,Response
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/process": {"origins": "http://localhost:port"}})

@app.route('/',methods= ['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()