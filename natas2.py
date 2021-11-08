#!/usr/bin/env python

import requests
import re

username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

url = "http://%s.natas.labs.overthewire.org/files/users.txt" % username

response = requests.get(url, auth=(username, password))
content = response.text

nextlevelpass = re.findall("natas3:(.*)", content)


# we find npthing on the page so lets print the content
# so, the next step is to go for the files/users.txt
# it's there in the content so to print it in the same fashion
