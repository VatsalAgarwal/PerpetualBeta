import urllib.request
import re
import os
termstring = ""
print("This is a Wikipedia search engine. Please note that only queries matching exact pages will return results.")

term = str(input("Please enter search term : "))

termfilt = re.split(r'\s*',term) #To split spaces

print(termfilt)
print(len(termfilt))
print(type(termfilt))

x = len(termfilt)
'''
The following code is in accordance with Wikipedia's search template, wherein an underscore '_' is appended to every term after a space
'''

if (len(termfilt)==1):
	print("")
elif(len(termfilt)>1):
	for i in range(0,x):
		term = termfilt[i]+"_"
		termstring = termstring+term
		termfinal = termstring[:len(termstring)-1]
print(termfinal)
		
url  = 'https://en.wikipedia.org/wiki/'+termfinal

# Just two different ways of doing the exact same thing, but I'll be using the 
# second one; It saves us the hassle of specifying a filename. Both snippets 
# of code allow us to save the extracted text in a file for further parsing 
# with regular expressions.
'''
one = urllib.request.urlopen(url) 
text1 = str(one.read())
with open("file1.txt","w") as outfile:
	outfile.write(text1)
text = re.findall(r'p>(*)</p>',file1.txt)
print(text)
'''

link = urllib.request.urlopen(url)
text1 = str(link.read())
filename = termfinal+".txt"
with open(filename,"w") as outfile:
        outfile.write(text1)

resultunfilt= re.findall(r'<p>(*)</p>',filename)
file1 = termfinal+"1.txt"
with open("file1","w") as test:
        test.write(resultunfilt)

# Of course, this can be further filtered and simplified to obtain human-
# readable text. But my initial purpose was simply to create a utility to obtain# Wikipedia text from the commandline.  







	
