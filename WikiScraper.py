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


def createJSON(toJSON, outputFile):
    json_obj = json.dumps(toJSON, indent=4)
    with open(outputFile, 'w') as outfile:
        outfile.write(json_obj)


def listToInt(toConvert):
    toReturn = ''
    for i in toConvert:
        toReturn += i
    return int(toReturn)


# from wikiciteparser.parser import parse_citation_template
print('Enter the Wikipedia URL: ')
url = input()  # Example URL
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
citations = soup.find_all('li', id=re.compile('cite_note'))

print("\nList of external articles: ")
extArts = soup.find_all(class_=['citation web cs1', 'citation news cs1', 'citation pressrelease cs1'])
ExtArticle = 1

# for spanTag in soup.find_all('span', class_='reference-accessdate'):
#     if spanTag.find_previous_sibling("a") is None:
#         pass
#     else:
#         if (len(spanTag.contents) > 2):
#             if "book" in spanTag.find_previous_sibling("a").get('href'):
#                 # print("Error Condition")
#                 # No op, fall through
#                 pass
#             else:
#                 print(ExtArticle, "Retrieved on:", spanTag.contents[1].string, spanTag.contents[2], "    URL:    ",
#                       spanTag.find_previous_sibling("a").get('href'), "  RefID:  ")
#         # else:
#         #     print(ExtArticle, "Retrieved on:", spanTag.contents[1].contents, "Different date format", "URL:    ",
#         #           spanTag.find_previous_sibling("a").get('href'), "  RefID:  ")
#         ExtArticle += 1

extURLS = []
extTitles = []
extRefID = []
artRefs = []
extDates = []

for artRef in extArts:
    artRefs.append(artRef)
    if artRef.a.text.startswith('"'):
        extTitle = artRef.a.text
    else:
        tmp = artRef.find_all(class_="external text")
        extTitle = tmp[0].text
    href_tags = artRef.find_all(href=True)
    tag = href_tags[0].attrs['href']
    if tag.startswith('/wiki'):
        artURL = 'https://en.wikipedia.org/wiki' + tag
    else:
        artURL = tag
    tag = artRef.find_all(class_='reference-accessdate')
    if tag:
        artContent = tag[0].contents
        if len(artContent) > 1:
            artDate = artContent[1].text + artContent[2]
        else:
            tmp = artContent[0]
            tmpDate = tmp.split('Retrieved ')
            artDate = tmpDate[1]
    else:
        artDate = 'NULL'
    extHash = hash(artURL)

    extRefID.append(extHash)
    extDates.append(artDate)
    extURLS.append(artURL)
    extTitles.append(extTitle)

print("\nList of books: ")
# print(soup.find_all('bdi'))
bookId = 1
ISBN = []
bookAuthors = []
bookTitles = []
bookRefID = []
bookPublishers = []
bookRefs = []
for bookRef in soup.find_all(class_='citation book cs1'):
    bookRefs.append(bookRef)
    if bookRef.findAll(text="ISBN"):
        bookTitle = bookRef.i.string
        relevantStr = bookRef.text
        bookStr = relevantStr.split('(')
        bookAuthorInst = bookStr[0]

        remStr = bookStr[1].split('.')
        if len(remStr) > 2:
            publisher = remStr[2]
        else:
            publisherArr = bookStr[2].split('.')
            publisher = publisherArr[1]

        hashStr = bookTitle + bookAuthorInst
        bookHash = hash(hashStr)
        isbnRefStr = bookRef.text.split('ISBN')
        isbnList = list(filter(str.isdigit, isbnRefStr[1]))
        isbnInt = listToInt(isbnList)
        #  Add all results to arrays
        ISBN.append(isbnInt)
        bookTitles.append(bookTitle)
        bookAuthors.append(bookAuthorInst)
        bookPublishers.append(publisher)
        bookRefID.append(bookHash)

print("\nList of scientific papers")
sciCount = 0  # To count the number of papers cited
sciRefs = soup.find_all('cite', class_='citation journal cs1')

trueSciRefs = []  # This contains only the actual BeautifulSoup elements that contain genuine scientific papers.
titles = []  # Array with titles of scientific papers. Same for authors and dates below.
authors = []
dates = []
refID = []
journals = []
testInt = 0

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
        if '(' in authorList:
            sciDate = re.search(r'\((.*?)\)', authorList).group(1)  # Regex to get the date which is enclosed in parentheses
        else:
            sciDate = 'NULL'
        sciAuthors = authorList.split('(')
        sciAuthors = sciAuthors[0]
        hashCode = hash(titles[sciCount - 1])
        authors.append(sciAuthors)
        dates.append(sciDate)
        journals.append(aTag.i.string)
        refID.append(hashCode)
        print(str(sciCount) + ": Title: " + titles[sciCount - 1] + "; Published on: " + str(
            sciDate) + "; Authors: " + sciAuthors + "; RefID: " + str(hashCode))


jsonData = {'Scientific Papers': [], 'Books': [], 'External Articles': []}
for i in range(0, len(journals)):
    jsonData['Scientific Papers'].append({
        'WikiURL': str(url),
        'count': i + 1,
        'Title': titles[i],
        'Authors': authors[i],
        'Published Date': dates[i],
        'Journal': journals[i],
        'refID': refID[i]
    })

for i in range(0, len(bookAuthors)):
    jsonData['Books'].append({
        'WikiURL': str(url),
        'count': i + 1,
        'Title': bookTitles[i],
        'Authors': bookAuthors[i],
        'Publisher': bookPublishers[i],
        'ISBN': ISBN[i],
        'refID': bookRefID[i]
    })

for i in range(0, len(extURLS)):
    jsonData['External Articles'].append({
        'WikiURL': str(url),
        'count': i + 1,
        'Title': extTitles[i],
        'Retrieval Date': extDates[i],
        'Article URL': extURLS[i],
        'refID': extRefID[i]
    })

print('\n')
print('Please enter the desired output filename:')
outputFile = input()
createJSON(jsonData, outputFile + '.txt')
