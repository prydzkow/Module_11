**<span style="text-decoration:underline;">Authentication</span>**

We can encode a ‘string’ like this:


```
echo 'admin:Cisco123' | base64
```


… and decode it like this:


```
echo 4oCYYWRtaW46Q2lzY28xMjPigJkK | base64 -d
```


Note the use -D BSD/Mac and -d for Linux



*   [OAuth](https://en.wikipedia.org/wiki/OAuth) on Wikipedia

**<span style="text-decoration:underline;">Tools</span>**

Take a look at some examples in:



*   Firefox
*   Postman
*   cURL

Deck of cards example:


```
https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1
```


DNA Center Sandbox:


```
https://sandboxdnac.cisco.com/
```


Credentials: ‘devnetuser:Cisco123!’

OpenAPI Example:


```
https://developer.webex.com/docs/api/v1/messages/create-a-message
```


**<span style="text-decoration:underline;">Python Requests</span>**

DNAC Rest API Example:

  <tr>
   <td>

```
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
```


   </td>
  </tr>