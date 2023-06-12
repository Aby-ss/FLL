import http.client
from rich.pretty import pprint

conn = http.client.HTTPSConnection("api.ambeedata.com")

headers = {
    'x-api-key': "0f224f1547e7f994559ef153134453aecf2a16904e9fbd9bf111fe4ed8434dad",
    'Content-type': "application/json"
    }

conn.request("GET", "/weather/forecast/by-lat-lng?lat=12.9889055&lng=77.574044", headers=headers)

res = conn.getresponse()
data = res.read()

pprint(data.decode("utf-8"), expand_all=True)