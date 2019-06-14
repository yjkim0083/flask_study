from flask import Flask, jsonify
from flask_cors import CORS
import csv
import numpy as np
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    print(time.time())
    x, y, label = csvParser()
    print(time.time())
    return jsonify(x=x, y=y, label=label)

def csvParser():
    data_path="tSNE-example8.csv"
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)
        data = list(reader)

    # convert list to npdarray
    _data = np.array(data)
    x = _data[:, 1:2].flatten().tolist()
    y = _data[:, 2:3].flatten().tolist()
    label = _data[:, -1:].flatten().tolist()

    return x, y, label

if __name__ == '__main__':
    app.run()
