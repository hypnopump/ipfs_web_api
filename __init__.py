# -*- coding: iso-8859-15 -
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
	return "IPFS Decentralized Webpages Under Construction"

@app.route('/add/<name>/<link>/')
def add(name, link):
	if record(name, link):
		return "SUCCESS!"

@app.route('/search/<query>/')
def queried(query):
	return search(query)

def search(query):
	sols = []
	with open('records/records.txt', 'r') as f:
		r = f.readlines()
	for line in r:
		if len(line) > 2:
			args = line.split(',')
			if query in args[0].split(' '):
				sols.append({"name": args[0]}, args[1])
	output = {"results":}
	return str({"data": {"id": "42","username": "zbeeble","full_name": "Zaphod Beeblebrox","be_like": ["Yahweh","The Messiah","Godzilla"],"like_tags": ["landscape","adventure"]}})

def record(name, link):
	with open('records/records.txt', 'w+') as f:
		f.write(name+',https://'+link)
	return True


		

if __name__ == '__main__':
    # Deploying
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
	# Debugging
	# app.run(debug=True, host='0.0.0.0')