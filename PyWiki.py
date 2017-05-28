import requests
from bs4 import BeautifulSoup as bs

print("\nWelcome to PyWiki v1.0.\n\nThis utility returns the introductory paragraph\nfrom the Wikipedia article of your search, \nwhich is saved in a textfile of the same name.\n\n")
search = input(str("Please enter text here: "))
searchterm = search.split()

#To enforce Wikipedia search term standards in the URL:
#eg: A search for 'Bob Dylan' becomes :
#https://en.wikipedia.org/wiki/Bob_Dylan

if len(searchterm)>1:
	for i in range(0,len(searchterm)-1):
		search = searchterm[i]+"_"+searchterm[i+1]


url = "https://en.wikipedia.org/wiki/"+search
print(url)

info = requests.get(url)
soup = bs(info.content, 'html.parser') 
#print(soup.prettify)

first = ''.join(text.strip() for text in soup.p.find_all(text=True, recursive=False))

print(first)

with open(search, "w") as file:
	file.write(first)
