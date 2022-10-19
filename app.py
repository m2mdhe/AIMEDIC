from flask import Flask, request, render_template, jsonify
from backend.symptoms import *
import json

b,c,d = None, None, None

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("main.html")

@app.route('/search-symp', methods = ['POST'])
def search():
	global b, c, d
	data = request.get_json()['symptoms']
	a,b,c,d = solver(data)
	return jsonify(a)

@app.route('/find-diagnostic', methods = ['POST'])
def super():
	data = request.get_json()['symptoms']
	print(data)

	return react_out(data, b, c, d)

if __name__ == '__main__':
   app.run(debug = True, port=3000)