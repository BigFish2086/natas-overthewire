#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

post_data = {"secret": "oubWYf2kBq", "submit": "submit"}

# for the main page
response = session.post(url, data=post_data, auth=(username, password))

# for the /index-source.html page
# response = session.get(url, auth=(username, password))

content = response.text
soup = BeautifulSoup(content, "html.parser")

print(soup.prettify())
# print content

# this has a 'viewsource' anchour tag directs us to /index-source.html
# this time we need a  php script to help us it's natas.php
# to try to decode the { $encodedSecret } ---> { oubWYf2kBq }
# and we now have access The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
