# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests
import pandas as pd
requests.packages.urllib3.disable_warnings()

url 		= "https://www.formula1.com/en/championship/drivers.html"
Name 		= []
URL 		= []

soup 		= BeautifulSoup(urlopen(url),'lxml')
print(soup)
right_table = soup.find('td', {"class": "name_"})
	

print(right_table)
# for letter in alphabet:
# 	print(url + letter)
# 	list_players 	= right_table.findAll("p")
# 	for row in list_players:

# 		name = row.find('a')
# 		name = name.find(text = True).encode('utf-8')
# 		if name not in Name:
# 			Name.append(name)
# 			some = row.find('a')
# 			years = row.encode('utf-8').split('(')[1].split(')')[0]
# 			Stear.append(years.split('-')[0])
# 			Enear.append(years.split('-')[1])
# 			some = some["href"]
# 			URL.append(some)
# 			print("Done for " + name)

# df = pd.DataFrame({
# 	"Name" 	: Name,
# 	"Url"	: URL,
# 	"Stear" : Stear,
# 	"Enear" : Enear
# 	})

# df.to_csv("Players.csv", index = False)