import json
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
url = 'https://en.wikipedia.org/wiki/Facebook'  # Example URL
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
        print(bookId, ":    ", "    ISBN:    ", bditag.parent.contents[0].string, "   Authors:    ",
              bditag.parent.parent.contents[0].string, " Title:   ", bditag.parent.find_previous_sibling('i').contents,
              "  RefID:  ", uuidOne)
    # print(bookId, ":    ", "    ISBN:    ", bditag.parent.contents[0].string, "   Authors:    ", bditag.parent.parent.contents[0].string)
    bookId += 1

print("\nList of scientific papers")
sciCount = 0  # To count the number of papers cited
sciRefs = soup.find_all('cite', class_='citation journal cs1')

trueSciRefs = []  # This contains only the actual BeautifulSoup elements that contain genuine scientific papers.
titles = []  # Array with titles of scientific papers. Same for authors and dates below.
authors = []
dates = []
refID = []
journals = []

# Attributes needed: Title, Authors, RefId, WikiURL, Name, journal; need: institution, field, ID (DOI)
for aTag in sciRefs:
    authorList = aTag.contents[0].string
    if aTag.findAll(text="doi"):
        trueSciRefs.append(aTag)
        sciCount += 1
        str1 = aTag.a.string
        # Papers store their titles in one of two locations, need to check
        if str1 == 'doi' or str1 == 'arXiv' or str1 == 'Bibcode':
            authorL = aTag.contents[0].string
            title = re.split('(")', authorL)
            titles.append(title[2])
        else:
            titles.append(str1)
        sciDate = re.search(r'\((.*?)\)', authorList).group(1)  # Regex to get the date which is enclosed in parentheses
        sciAuthors = authorList.split('(')
        sciAuthors = sciAuthors[0]
        hashCode = hash(titles[sciCount - 1])
        authors.append(sciAuthors)
        dates.append(sciDate)
        journals.append(aTag.i.string)
        refID.append(hashCode)
        print(str(sciCount) + ": Title: " + titles[sciCount - 1] + "; Published on: " + str(
            sciDate) + "; Authors: " + sciAuthors + "; RefID: " + str(hashCode))
jsonSci = {}
jsonSci['Scientific Papers'] = []
for i in range (0, len(journals)):
    jsonSci['Scientific Papers'].append({
        'WikiURL': str(url),
        'count': i + 1,
        'Title': titles[i],
        'Authors': authors[i],
        'Published Date': dates[i],
        'Journal': journals[i],
        'refID': refID[i]
    })

json_obj = json.dumps(jsonSci, indent=4)

with open('jsonSci.txt', 'w') as outfile:
    outfile.write(json_obj)