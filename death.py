import requests
from bs4 import BeautifulSoup as bs

# URL for the US Supreme Court Website :

url = requests.get("https://www.tdcj.state.tx.us/death_row/dr_offenders_on_dr.html")

soup = bs(url.content, 'html.parser')

table = soup.find_all('div', attr= {'class':'return_to_div'})
print(table)

