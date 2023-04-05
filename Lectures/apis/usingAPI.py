from flask import Flask

HOST = "localhost" # 127.0.0.1
PORT = 1234
DEBUG = True

app = Flask(__name__)

@app.route("/first", methods=['GET']) # get request
def firstRoute():
    return "My first route!"

@app.route("/new", methods=['GET']) # get request
def test():
    return "new"

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)