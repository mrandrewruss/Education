import requests

response = requests.get("http://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
print(response.text)


# response = requests.post("http://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# print(response.text)