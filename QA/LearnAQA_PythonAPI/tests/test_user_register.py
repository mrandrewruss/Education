import requests
from QA.LearnAQA_PythonAPI.lib.base_case import BaseCase
from QA.LearnAQA_PythonAPI.lib.assertions import Assertions

class TestUserRegister(BaseCase):
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'email': email,
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exests", f"Unexpected response content {response.content}"