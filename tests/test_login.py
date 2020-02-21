from datetime import datetime

import pytest

from ..steps.login import Login


@pytest.mark.login
class TestLogin:
    
    login = Login()

    def test_login_valid_credentials(self, creating_new_user):
        self.login.post_request(
            data={'email': creating_new_user['user_email'],
                  'password': creating_new_user['password']})
        self.login.should_be_status_code_200()
        self.login.should_be_text_result_true()

    def test_login_invalid_password(self, creating_new_user):
        wrong_password = datetime.now().strftime("Hello%d%m%Y-%H-%M-%S-%f")
        self.login.post_request(
            data={'email': creating_new_user['user_email'],
                  'password': wrong_password})
        self.login.should_be_status_code_200()
        self.login.should_be_text_result_false()

    def test_login_invalid_email(self, creating_new_user):
        wrong_user_email = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f") + '@test.test'
        self.login.post_request(data={'email': wrong_user_email, 'password': creating_new_user['password']})
        self.login.should_be_status_code_200()
        self.login.should_be_text_result_false()

    def test_login_invalid_credentials(self, creating_new_user):
        wrong_user_email = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f") + '@test.test'
        wrong_password = datetime.now().strftime("Hello%d%m%Y-%H-%M-%S-%f")
        self.login.post_request(data={'email': wrong_user_email, 'password': wrong_password})
        self.login.should_be_status_code_200()
        self.login.should_be_text_result_false()
