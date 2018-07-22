from bs4 import BeautifulSoup
import urllib2

titles = []
dates = []
scores = []

url = "http://ca.ign.com/reviews/games?"
f = urllib2.urlopen(url)

text = f.read()

soup = BeautifulSoup(text, 'html.parser')


tags = soup.find_all('div', class_='clear itemList-item')

for tag in tags:
    titles.append(tag.h3.a.text)
    dates.append(tag.find(lambda t: t.name == 'div' and t.get('class') == ['grid_3']).div.text)
    scores.append(tag.find('span', class_="scoreBox-score").text)

dic = {}

for ind, title in enumerate(titles):
    dic.setdefault('Game %d' % ind, {})['Title'] = title
    dic.setdefault('Game %d' % ind, {})['Date'] = dates[ind]
    dic.setdefault('Game %d' % ind, {})[''] = scores[ind]

for key, val in dic.iteritems():
    print val
