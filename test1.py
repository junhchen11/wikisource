import requests
import urllib.request
import time #for eventually using the 'date of retrieval' of a reference
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import sys
from urllib.request import urlopen
import mwparserfromhell
# from wikiciteparser.parser import parse_citation_template
url = 'https://en.wikipedia.org/wiki/Database' #Example URL
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
citations = soup.find_all('cite') #Exploring the CSS of the wikipedia website shows that references are stored under the 'cite' class.
references = []
info=[]

for spanTag in soup.find_all('span',class_='reference-accessdate'):
    # print(spanTag.parent.contents[0], spanTag.contents[1].contents)
    if (len(spanTag.contents)>2):
        print(spanTag.contents[2])
    else:
        print(spanTag.parent, "No year")

# sys.exit()

# print(soup.find_all('bdi'))
bookId=0
for bditag in soup.find_all('bdi'):
    # print(bookId, ":    ", bditag.parent.parent, bditag.contents)
    print(bookId, ":    ", bditag.parent.parent.contents[0], bditag.parent['title'], bditag.contents)
    bookId+=1

# for ref in citations:    
    # print(ref.contents)
    # if "Tsitchizris" in ref.contents[0]:
            # print("cite:", len(ref.contents[5].children))
            # print("cite: ", ref.contents[5].contents[0].name)
    #references.append(ref.a.get('href')) #references links are stored in the format href = <link>. These are stored under something called "a", so reference.a contains href = <link>
    #info.append(ref.cite.nextsibling)

#print('The no. of references is: ' + str(len(references)))
#for i in range(1, 27):
#    print(references[i])
#    print(info[i])
# wikicode = mwparserfromhell.parse(references)
# for tpl in wikicode.filter_templates():
#     parsed = parse_citation_template(tpl)
#     print(parsed)