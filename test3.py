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

for ref in citations:
    references.append(ref.a.get('href')) #references links are stored in the format href = <link>. These are stored under something called "a", so reference.a contains href = <link>
print('The no. of references is: ' + str(len(references)))
# for i in range(1, 10):
#     print(references[i])

print("\nList of external articles: ")
ExtArticle=1
for spanTag in soup.find_all('span',class_='reference-accessdate'):
    if (len(spanTag.contents)>2):
        print(ExtArticle, "Retrieved on:", spanTag.contents[1].string, spanTag.contents[2],  "    URL:    ", spanTag.find_previous_sibling("a").get('href'), "  RefID:  ", spanTag.parent.parent.parent.get('id'))
    else:
        print(ExtArticle, "Retrieved on:", spanTag.contents[1].contents, "Different date format",  "URL:    ",  spanTag.find_previous_sibling("a").get('href'), "  RefID:  ", spanTag.parent.parent.parent.get('id'))
    ExtArticle+=1

print("\nList of books: ")
# print(soup.find_all('bdi'))
bookId=1
for bditag in soup.find_all('bdi'):
    print(bookId, ":    ", "    ISBN:    ", bditag.parent.contents[0].string, "   Authors:    ", bditag.parent.parent.contents[0].string)
    bookId+=1


    
print("\nList of scientific papers")
scId=1
for aTag in soup.find_all('cite', class_='citation journal cs1'):
    print(scId, ":","       Authors: ", aTag.contents[0].string)
    scId+=1