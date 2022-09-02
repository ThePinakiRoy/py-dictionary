import json
import urllib.request

with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
    data = json.load(url)
    print(data)