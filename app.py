from flask import Flask, jsonify, render_template
from script import fetch_data, FetchFunction
import datetime

app = Flask(__name__)

@app.route('/api/tables/ign', methods=['GET'])
def get_ign_tables():
	ign = fetch_data('http://ca.ign.com/reviews/games?sortBy=score&time=3m', FetchFunction.IGN)

	dic={
			'reviewer' : 'IGN',
			'time_requested' : datetime.datetime.now(),
			'table' : ign.values.tolist()
		}

	return jsonify(dic)

@app.route('/api/tables/metacritic', methods=['GET'])
def get_metacritic_tables():
	metacritic = fetch_data('http://www.metacritic.com/browse/games/score/metascore/90day/all/filtered', FetchFunction.METACRITIC)

	dic={
			'reviewer' : 'Metacritic',
			'time_requested' : datetime.datetime.now(),
			'table' : metacritic.values.tolist()
		}				

	return jsonify(dic)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')