# -*- coding: iso-8859-15 -
from flask_cors import CORS, cross_origin
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import os
import json

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
vault = "static/data/records.txt"


@app.route('/')
def home():
    return "IPFS Decentralized Webpages Under Construction"

@cross_origin()
@app.route('/add/<name>/<link>/')
def add(name, link):
    if record(name, link):
        return "SUCCESS!"

@cross_origin()
@app.route('/search/<query>/')
def queried(query):
    return search(query)

@cross_origin()
@app.route('/<error>/')
def err(error):
    return "Error"


def search(query):
    sols = []
    with open(vault, 'r') as f:
        r = f.readlines()
    for line in r:
        if len(line) > 2:
            args = line.split(',')
            if query in args[0].split(' '):
                sols.append({"name": args[0],"link": args[1][:-2]})
    return json.dumps(sols)

def record(name, link):
    with open(vault, 'a') as f:
        f.write(name + ',https://ipfs.io/ipfs/' + link + "\n")
    return True


if __name__ == '__main__':
    # Deploying
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # Debugging
    # app.run(debug=True, host='0.0.0.0')
