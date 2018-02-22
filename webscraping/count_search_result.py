#! /usr/bin/python3
"""
Python script for sending a HTTP POST request to a web search form,
then scrape the result and print out total number of search results
"""
import urllib
from bs4 import BeautifulSoup

url = ""  # fill in the test url here
post_params = {
    'Birth date': '19000101',
    'Family name': 'De Jong'
}
post_args = urllib.urlencode(post_params)

fp = urllib.urlopen(url, post_args)
soup = BeautifulSoup(fp, "html5lib")
results = soup.find_all('h4', id="search_result")

print("Total number of search result is ") + str(len(results))
