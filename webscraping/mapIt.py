#!/usr/bin/python3
# mapit.py - Launches a map in the browser using
# command line argument or clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from the command line
    address = ''.join(sys.argv[1:])
else:
    # Get address from the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
