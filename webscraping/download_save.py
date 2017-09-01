#!/usr/bin/python3
# fetch a file from web and save it locally
import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
try:
    res.raise_for_status()
except Exception as exc:
    print("There is a problem: %s" % (exc))

f = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    f.write(chunk)
f.close()
