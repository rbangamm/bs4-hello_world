from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import re

def fetch_data(url, process_func):
	titles = []
	dates = []
	scores = []
	platforms = []

	request = urllib.request.Request(url, None, {'User-Agent' : 'Mozilla'})

	f = urllib.request.urlopen(request)

	text = f.read()

	soup = BeautifulSoup(text, 'html.parser')

	process_func(soup, titles, dates, scores, platforms)

	dic = {'Title' : titles, 'Date' : dates, 'Platform' : platforms, 'Score' : scores}
	df = pd.DataFrame(data=dic)

	return df

def process_ign(soup, titles, dates, scores, platforms):

	tags = soup.find_all('div', class_='clear itemList-item')

	for tag in tags:
	   t = tag.h3.a.text
	   match = re.search('\s*(.*)\s*', t)
	   titles.append(match.group(1))
	   dates.append(tag.find(lambda t: t.name == 'div' and t.get('class') == ['grid_3']).div.text)
	   scores.append(tag.find('span', class_="scoreBox-score").text)
	   platforms.append(tag.find('span', class_="item-platform").text)

def process_metacritic(soup, titles, dates, scores, platforms):

	tags = soup.find_all('div', class_='product_row game', limit=25)

	for tag in tags:
		match = re.search('\s*(.+)\s*\((\w+)\)', tag.find('div', class_='product_item product_title').a.text)
		titles.append(match.group(1))
		platforms.append(match.group(2))
		scores.append(tag.find('div', class_='product_item product_score').div.text)
		dates.append(tag.find('div', class_='product_item product_date').text)