from flask import Flask, jsonify, request
import json

HOST = "localhost" # 127.0.0.1
PORT = 1234
DEBUG = True

app = Flask(__name__)


# ROUTES START #
@app.route("/first", methods=['GET']) # get request
def firstRoute():
    return jsonify({"response":"My first route!"})



@app.route("/numberInspector", methods=["POST"])
def numberInspector():
    userInput = request.json["value"]
    # looking for an integer
    if type(userInput) == int:
        try:
            return getDataFor(str(userInput))
        except KeyError:
            return createDataFor(userInput)
    else:
        return jsonify({"results": f"the \"value\" should be an int"}), 400

@app.route("/new", methods=['GET']) # get request
def test():
    return "new"

# ROUTES END #

def createDataFor(value):
    data = load_data()
    data[value] = {
            "iseven": value % 2 == 0,
            "square": value**2,
            "cube": value**3,
            "binary": bin(value),
            "hex": hex(value)
        }
    save_data(data)
    return data

def getDataFor(value):
    data = load_data()
    return data[value]

# function to load json
def load_data():
    with open("Lectures/apis/data.json", "r") as file:
        data = json.load(file)
    return data

# function to save data
def save_data(data):
    with open("Lectures/apis/data.json", "w") as file:
        json.dump(data, file)





if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)