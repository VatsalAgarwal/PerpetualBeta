import requests
from bs4 import BeautifulSoup as bs

url = requests.get("https://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html")

soup = bs(url.content, 'html.parser')
#print(soup.prettify)
execs = soup.find_all('table', attrs={'class':'os'})
#print(execs)

for i in execs:
	for row in i.find_all('th',attr={'scope':'col'}):
		print(row)


