from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import re

titles = []
dates = []
scores = []
platforms = []

url = "http://ca.ign.com/reviews/games?"
f = urllib.request.urlopen(url)

text = f.read()

soup = BeautifulSoup(text, 'html.parser')


tags = soup.find_all('div', class_='clear itemList-item')

for tag in tags:
   t = tag.h3.a.text
   match = re.search('\s*(.*)\s*', t)
   titles.append(match.group(1))
   dates.append(tag.find(lambda t: t.name == 'div' and t.get('class') == ['grid_3']).div.text)
   scores.append(tag.find('span', class_="scoreBox-score").text)
   platforms.append(tag.find('span', class_="item-platform").text)

dic = {'Title' : titles, 'Date' : dates, 'Platform' : platforms, 'Score' : scores}

df = pd.DataFrame(data=dic)

print(df)