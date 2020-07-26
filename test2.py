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
    # print(references[i])

print("\nList of external articles: ")
ExtArticle=1
for spanTag in soup.find_all('span',class_='reference-accessdate'):
    # print(ExtArticle,  ":    ", spanTag.parent.contents[0], "Retrieved on:", spanTag.contents[1].contents)
    # print(spanTag.parent.contents[0], spanTag.contents[1].contents)
    if (len(spanTag.contents)>2):
        print(ExtArticle, "Retrieved on:", spanTag.contents[1].contents, spanTag.contents[2],  "    URL:    ", spanTag.parent.contents[0])
    else:
        print(ExtArticle, "Retrieved on:", spanTag.contents[1].contents, "No year",  "URL:    ", spanTag.parent.contents[0])
    ExtArticle+=1

print("\nList of books: ")
# print(soup.find_all('bdi'))
bookId=1
for bditag in soup.find_all('bdi'):
<<<<<<< HEAD
        # print(bookId, ":    ", bditag.parent.parent, bditag.contents)
        # print(bookId, ":    ", bditag.parent.parent.contents[0], bditag.parent['title'], bditag.contents)
        # print(bookId, ":    ", "Authors:    ", bditag.parent.parent.contents[0], bditag.parent['title'], "  ISBN:   ", bditag.contents)
    print(bookId, ":    ", "    ISBN:    ", bditag.parent.contents[0].string, "   Authors:    ", bditag.parent.parent.contents[0].string)
    bookId+=1
# print("\nList of books")
# for bdiTag in soup.find_all('cite', class_='citation book cs1'):
#     print("Authors: ", bdiTag.contents[0].string, " ISBN:    ", bdiTag.contents)


    
print("\nList of scientific papers")
scId=1
for aTag in soup.find_all('cite', class_='citation journal cs1'):
    print(scId, ":","       Authors: ", aTag.contents[0].string)
    scId+=1
=======
    # print(bookId, ":    ", bditag.parent.parent, bditag.contents)
    # print(bookId, ":    ", bditag.parent.parent.contents[0], bditag.parent['title'], bditag.contents)
    # print(bookId, ":    ", "Authors:    ", bditag.parent.parent.contents[0], bditag.parent['title'], "  ISBN:   ", bditag.contents)
    print(bookId, ":    ", "ISBN:   ", bditag.contents, "   Authors:    ", bditag.parent.parent.contents[0], "    URL:    ", bditag.parent.parent.contents[0])
    bookId+=1

    
print("\nList of scientific papers")
for aTag in soup.find_all('cite', class_='citation journal cs1'):
    print("Authors: ", aTag.contents[0].string)
    
>>>>>>> b5152de8249f5a5e47c3f8f1a31944a2e9e28a2f
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
<<<<<<< HEAD
#     print(parsed)
=======
#     print(parsed)
>>>>>>> b5152de8249f5a5e47c3f8f1a31944a2e9e28a2f
