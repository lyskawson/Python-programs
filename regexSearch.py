#!/usr/bin/env python3

import os, re


files = os.listdir(os.getcwd()) # same as os.listdir('.')
txt_files = []

txt_regex = re.compile(r'.txt')

#filter only txt documents 
for doc in files:
    if txt_regex.search(doc) is not None:
        txt_files.append(doc)

# phone num search
searchRegex = re.compile(r'''(
    [a-zA-Z0-9.-_%+]+    # user name
    @                    # at
    [a-zA-Z0-9.-]+       # domain name    
    (\.[a-zA-Z]{2,4})    # dot and something  
    )''', re.VERBOSE)   # Matches all words ending in !

found = []
for doc in txt_files:
    openedFile = open(doc)
    contents = openedFile.read()
    
    found = searchRegex.findall(contents)
    found.append(doc[0])
    result = '\n'.join('\n'.join(tup) for tup in found)
print(result)