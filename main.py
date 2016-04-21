import argparse
import logging
import json
import sys
import re
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

from urllib.request import urlopen, Request

parser = argparse.ArgumentParser(description="Encrypts variables for Travis")
parser.add_argument("--org, --user", required=True, help="The username or organisation your repository is for", dest='org')
parser.add_argument("--repo", required=True, help="The repository", dest='repo')
parser.add_argument("text", metavar='Text' ,help="The string that needs encrypting")

args = parser.parse_args().__dict__

org = args['org']
repo = args['repo']
text = args['text']

public_key = str
# Get public key from Travis
url = 'https://api.travis-ci.org/repos/'+org+'/'+repo+'/key'
logging.info('Querying ' + url)
request = Request(url)
with urlopen(request) as response:
    if response.status == 200:
        # Get response as a string rather than a series of bytes
        str_response = response.read().decode('utf-8')
        jsonified = json.loads(str_response)
        public_key = jsonified['key']
        public_key = RSA.importKey(public_key)
    else:
        logging.warning(response.status)
        sys.exit()

# Cipher
cipher = PKCS1_v1_5.new(public_key)

# Encoded text encoded as UTF-8 (bytes) => ciphertext (bytes) => base 64 ciphertext (bytes) => string
encrypted = binascii.b2a_base64(cipher.encrypt(text.encode())).decode()

print('- secure: ' + encrypted)