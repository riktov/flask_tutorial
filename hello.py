from flask import Flask 

print("Hello, Flask")

app = Flask(__name__)

@app.route('/')
def hello() :
    return 'Hello, Flask'
    