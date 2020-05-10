import requests

url = 'http://localhost:8080/api'
r = requests.post(url, json = {"x" : ['I hate harry potter']})
print(r.json())