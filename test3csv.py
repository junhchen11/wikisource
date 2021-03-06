import re
import requests
import urllib.request
import time  # for eventually using the 'date of retrieval' of a reference
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import sys
from urllib.request import urlopen
import uuid

# from wikiciteparser.parser import parse_citation_template
url = 'https://en.wikipedia.org/wiki/Database'  # Example URL
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
citations = soup.find_all(
    'cite')  # Exploring the CSS of the wikipedia website shows that references are stored under the 'cite' class.
references = []
uuidOne = uuid.uuid1()

for ref in citations:
    references.append(ref.a.get('href'))  # references links are stored in the format href = <link>. These are stored under something called "a", so reference.a contains href = <link>
print('The no. of references is: ' + str(len(references)))
# for i in range(1, 10):
#     print(references[i])

print("\nList of external articles: ")
ExtArticle = 1
substring1 = "Book"
# substring2 = "Retrieved"  substring2 not in spanTag.contents:
for spanTag in soup.find_all('span', class_='reference-accessdate'):
    if spanTag.find_previous_sibling("a") is None:
        pass
    else:
        if (len(spanTag.contents) > 2):
            if substring1 in spanTag.find_previous_sibling("a").get('href'): 
            # print("Error Condition")
            # No op, fall through
                pass
            else:
                print(ExtArticle, "Retrieved on:", spanTag.contents[1].string, spanTag.contents[2], "    URL:    ", spanTag.find_previous_sibling("a").get('href'), "  RefID:  ", uuidOne)
        else:
            print(ExtArticle, "Retrieved on:", spanTag.contents[1].contents, "Different date format", "URL:    ", spanTag.find_previous_sibling("a").get('href'), "  RefID:  ", uuidOne)
        ExtArticle += 1

print("\nList of books: ")
# print(soup.find_all('bdi'))
bookId = 1
for bditag in soup.find_all('bdi'):
    if bditag.parent.find_previous_sibling('i') is None:
        # print("Error condition")
        pass
    else:
        # print(bookId, ":    ", "    ISBN:    ", bditag.parent.contents[0].string, "   Authors:    ",
        #       bditag.parent.parent.contents[0].string, " Title:   ", bditag.parent.find_previous_sibling('i').contents,
        #       "  RefID:  ", uuidOne)
        d={'bookId': bookId, 'ISBN': bditag.parent.contents[0].string, 'Authors': bditag.parent.parent.contents[0].string, 'Title': bditag.parent.find_previous_sibling('i').contents, 'RefID':uuidOne}
        df = pd.DataFrame(data=d)
    bookId += 1
df.to_csv('foo.csv')
sys.exit()
        # print(bookId, ":    ", "    ISBN:    ", bditag.parent.contents[0].string, "   Authors:    ",
        #       bditag.parent.parent.contents[0].string, " Title:   ", bditag.parent.find_previous_sibling('i').contents,
        #       "  RefID:  ", uuidOne)
    # print(bookId, ":    ", "    ISBN:    ", bditag.parent.contents[0].string, "   Authors:    ", bditag.parent.parent.contents[0].string)
    


print("\nList of scientific papers")
scicount = 0
scirefs = soup.find_all('cite', class_='citation journal cs1')
titles = []
for aTag in scirefs:
    authorList = aTag.contents[0].string
    if "(" in authorList:
        scicount += 1
        str1 = aTag.a.string
        if str1 == 'doi' or str1 == 'arXiv' or str1 == 'Bibcode':
            authorL = aTag.contents[0].string
            title = re.split('(")', authorL)
            titles.append(title[2])
        else:
            titles.append(str1)
        sciDate = re.search(r'\((.*?)\)', authorList).group(1)
        sciAuthors = authorList.split('(')
        sciAuthors = sciAuthors[0]
        hashCode = hash(titles[scicount - 1])
        print(str(scicount) + ": Title: " + titles[scicount - 1] + "; Published on: " + str(
            sciDate) + "; Authors: " + sciAuthors + "; RefID: " + str(hashCode))
