
from flask import Flask

app = Flask(__name__) 

@app.route('/')
def home():
    return "pong"

@app.route('/ping', methods=['GET'])
def ping():
    return "pong"

app.run(debug=True, host='0.0.0.0', port=8787) 
