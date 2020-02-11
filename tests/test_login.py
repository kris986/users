from datetime import datetime

import pytest

from ..set_urls import DO_LOGIN
from ..steps.login import Login


@pytest.mark.login
class TestLogin:
    login = Login(DO_LOGIN)

    def test_login_valid_credentials(self, creating_new_user):
        response = self.login.sent_login_request(creating_new_user['user_email'], creating_new_user['password'])
        self.login.should_be_status_code_200(response)
        self.login.should_be_text_result_true(response)

    def test_login_invalid_password(self, creating_new_user):
        wrong_passwrd = datetime.now().strftime("Hello%d%m%Y-%H-%M-%S-%f")
        response = self.login.sent_login_request(creating_new_user['user_email'], wrong_passwrd)
        self.login.should_be_status_code_200(response)
        self.login.should_be_text_result_false(response)

    def test_login_invalid_email(self, creating_new_user):
        wrong_user_email = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f") + '@test.test'
        response = self.login.sent_login_request(wrong_user_email, creating_new_user['password'])
        self.login.should_be_status_code_200(response)
        self.login.should_be_text_result_false(response)
