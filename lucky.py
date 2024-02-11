#! /usr/bin/env python3


# The program doesn't work because the soup.select() 
#call returns an empty list since it can't find the search results in HTML.
import bs4, sys, webbrowser, requests

print('Searching...')
res = requests.get('https://google.pl/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")
linkElems = soup.select('p')

numOpen = min(3, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.pl' + linkElems[i].get('href'))

print(len(linkElems))

print('done')