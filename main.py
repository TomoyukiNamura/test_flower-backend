from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 
@app.route('/')
def hello():
    hello = "This is a test backend server."
    return hello
 
@app.route('/following')
def get_following():
    with open('testdata/following.txt', 'r') as f:
        result = f.read()
    return result

@app.route('/followers')
def get_followers():
    with open('testdata/followers.txt', 'r') as f:
        result = f.read()
    return result

if __name__ == "__main__":
    app.run()
