import requests

response = requests.get("http://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)

# Redirects
# Code: 300 & 301

response = requests.get("http://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
second_response = response

print(first_response.url)
print(second_response.url)