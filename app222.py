from flask import Flask, jsonify
from flask_cors import CORS
import json

import numpy as np
import csv

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    # csvParser()
    # #return 'Hello World!'
    # data = {
    #     "name":123,
    #     "age":444,
    #     "grade":1
    # }
    #return data
    #return Flask.Response(json.dumps(data), mimetype='application/json')
    return jsonify(result=csvParser())

def csvParser():
    data_path="hello.csv"
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)
        # _data = np.array(data).astype(float)
    return list(data)


if __name__ == '__main__':
    app.run()
