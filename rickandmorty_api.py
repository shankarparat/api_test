import requests


r = requests.get("https://rickandmortyapi.com/api")
apis = r.json()
c_r = requests.get(((apis["characters"])))
characters = (c_r.json())


status_dict = {}
for entry in characters["results"]:
    name = entry["name"]
    status = entry["status"]
    status_dict[name] = entry["id"],status

print(status_dict["Jerry Smith"])

locations_request = requests.get(apis["locations"])
locations = locations_request.json()

# for location in locations["results"]:
#