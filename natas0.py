#!/usr/bin/env python

import requests
import re

username = "natas0"
password = "natas0"

url = "http://%s.natas.labs.overthewire.org" % username

response = requests.get(url, auth=(username, password))
content = response.text

nextlevelpass = re.findall("<!--The password for natas1 is (.*) -->", content)

print(nextlevelpass[0])
