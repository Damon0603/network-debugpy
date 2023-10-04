import requests

BASE_URL = 'https://httpbin.org'

# data = {'data1': 'Hello', 'data2': 'world'}
# response = requests.post(BASE_URL + '/post', data=data)
#
# if response.status_code == 200:
#     print("Post request was successful")
# else:
#     print("failed")

username = 'testuser'
password = 'testpass'

response = requests.get(BASE_URL + f'/basic-auth/{username}/{password}', auth=(username, password))

if response.status_code == 200:
    print("GET request was successful")
else:
    print("failed")
