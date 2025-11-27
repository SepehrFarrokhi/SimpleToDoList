import requests

res = requests.put("http://127.0.0.1:5000/tags",
                   json = {"tag_name": "doongul"})

print(res.content)

