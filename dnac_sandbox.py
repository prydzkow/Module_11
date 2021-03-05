import requests
from requests.auth import HTTPBasicAuth
import json

DNAC_USER = 'devnetuser'
DNAC_PASSWORD = 'Cisco123!'


base_url = 'https://sandboxdnac.cisco.com'
token_url = '/dna/system/api/v1/auth/token'
resp = requests.post(base_url + token_url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD))
token = resp.json()['Token']


device_url = "/api/v1/network-device"
hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
resp = requests.get(base_url + device_url, headers=hdr)
device_list = resp.json()
print(json.dumps(device_list, indent=4))