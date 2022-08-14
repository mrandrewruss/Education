from libQA.my_requests import MyRequests
from libQA.base_case import BaseCase
from libQA.assertions import Assertions


class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        # POSITIVE TEST: CREATE USER WITH NEW EMAIL
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        # NEGATIVE TEST: CREATE USER WITH EXISTING EMAIL
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"
