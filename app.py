from flask import Flask, render_template
from script import fetch_data, FetchFunction

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	ign = fetch_data('http://ca.ign.com/reviews/games?sortBy=score&time=3m', FetchFunction.IGN)
	metacritic = fetch_data('http://www.metacritic.com/browse/games/score/metascore/90day/all/filtered', FetchFunction.METACRITIC)
	return render_template('index.html', ign=ign, metacritic=metacritic)
