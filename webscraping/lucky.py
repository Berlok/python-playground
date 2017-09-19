#!/usr/bin/python3
# I'm feeling lucky google search
import requests
import sys
import webbrowser
import bs4

print('Googling...')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1]))
res.raise_for_status()

# retrieve top search results
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# open a browser tab for each result
linkElems = soup.select('.r a')
tabsOpen = min(5, len(linkElems))  # maximal 5 tabs
for i in range(tabsOpen):
    webbrowser.open('https://www.google.com' + linkElems[i].get('href'))
