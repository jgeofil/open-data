#!/usr/bin/python3

"""
    get_categories.py

    MediaWiki API Demos
    Demo of `Categories` module: Get categories associated with a page.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "categories",
    "titles": "artificial intelligence",

    "cllimit": "max"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    for cat in v['categories']:
        print(cat["title"])