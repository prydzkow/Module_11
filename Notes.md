<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.442 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Fri Mar 05 2021 03:50:13 GMT-0800 (PST)
* Source doc: Netprog - Module 11
* This is a partial selection. Check to make sure intra-doc links work.
* Tables are currently converted to HTML tables.
----->


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