import requests

BASE_URL = 'https://httpbin.org'


response = requests.get(BASE_URL + '/get')
response = response.json()


del response["origin"]

print(response)