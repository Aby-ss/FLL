import http.client
from rich.pretty import pprint

conn = http.client.HTTPSConnection("api.ambeedata.com")

headers = {
    'x-api-key': "7eafc9fb1393d7456d0778e8bde486f02bcd494f87792146729bf4e61062ae36",
    'Content-type': "application/json"
    }

conn.request("GET", "/weather/forecast/by-lat-lng?lat=12.9889055&lng=77.574044", headers=headers)

res = conn.getresponse()
data = res.read()

pprint(data.decode("utf-8"), expand_all=True)