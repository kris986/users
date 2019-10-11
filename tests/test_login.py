from datetime import datetime

import pytest
from ..set_urls import DO_LOGIN
from ..steps.login import Login


@pytest.mark.login
class TestLogin:
    method = DO_LOGIN
    login = Login(method)

    @pytest.fixture(autouse=True)
    def setup(self):
        # self.user_name = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f") + '@test.test'
        self.user_name = '11.08.2019-23-06-59@test.test'
        self.password = '1234567'

    def test_login_valid_credentials(self):
        response = self.login.sent_login_request(self.user_name, self.password)
        self.login.should_be_status_code_200(response)
        self.login.should_be_text_result_true(response)

    def test_login_invalid_password(self):
        wrong_passwrd = datetime.now().strftime("Hello%d%m%Y-%H-%M-%S-%f")
        response = self.login.sent_login_request(self.user_name, wrong_passwrd)
        self.login.should_be_status_code_200(response)
        self.login.should_be_text_result_false(response)

    def test_login_invalid_email(self):
        wrong_user_email = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f") + '@test.test'
        response = self.login.sent_login_request(wrong_user_email, self.password)
        self.login.should_be_status_code_200(response)
        self.login.should_be_text_result_false(response)
