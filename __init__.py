# -*- coding: iso-8859-15 -
from flask_cors import CORS, cross_origin
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import json

app = Flask(__name__)
app.config.from_pyfile('utils/config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from utils import models
db.create_all()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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
	with open('records/records.txt', 'r') as f:
		r = f.readlines()
	for line in r:
		if len(line) > 2:
			args = line.split(',')
			if query in args[0].split(' '):
				sols.append({"name": args[0], "link": args[1]})
	return json.dumps(sols)
=======
    sols = []
    with open('records/records.txt', 'r') as f:
        r = f.readlines()
    for line in r:
        if len(line) > 2:
            args = line.split(',')
            if query in args[0].split(' '):
                sols.append({"name": args[0]}, args[1])
    output = {"results": }
    return json.dumps("data": {"id": "42", "username": "zbeeble", "full_name": "Zaphod Beeblebrox", "be_like": ["Yahweh", "The Messiah", "Godzilla"], "like_tags": ["landscape", "adventure"]})
>>>>>>> a9e979ff3da4c6930ab5edab270a3b384143d87e

=======
    sols = []
    q = models.Reg.query.all()
    for line in q:
        if query in line.name.split(" "):
            sols.append({"name": str(line.name),"link": str(line.hash)})
    return json.dumps(sols)
>>>>>>> 745a7103721c6d22a30992fafff05dfe32b4c859

def record(name, link):
    reg = models.Reg(name, "https://ipfs.io/ipfs/"+link+"/")
    db.session.add(reg)
    db.session.commit()
    return True


if __name__ == '__main__':
    # Deploying
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # Debugging
    # app.run(debug=True, host='0.0.0.0')
