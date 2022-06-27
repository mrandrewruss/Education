import requests

payload = {"login": "secret_login", "password": "secret_pass"}
responce1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
print(responce1.status_code)
print(dict(responce1.cookies))

cookie_value = responce1.cookies.get('auth_cookie')
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

responce2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(responce2.text)