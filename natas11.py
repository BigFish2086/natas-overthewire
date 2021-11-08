#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

cookie = {"data": "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

# for the main page
response = session.post(url, auth=(username, password), cookies=cookie)

# for the /index-source.html page
# response = session.get(url, auth=(username, password))

content = response.text
soup = BeautifulSoup(content, "html.parser")

get_data_cookie = session.cookies["data"]
# print get_data_cookie

print(soup)
# print content

# by going to source page /index-source.html
# we find a lot of encoding, so we need the help of php
# to simulate that encoding staff and then decode that back
# to get the right credits
# we first need the cookie
# data = ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw
# after executing some php code, we have the good cookie
# ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK
# and we are here to set the cookie using python
# and finally we have the password
# The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

