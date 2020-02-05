from datetime import datetime

import pytest

from ..steps.registration import Registration
from ..set_urls import DO_LOGIN, DOREGISTER
from ..steps.login import Login


@pytest.mark.login
class TestLogin:
    method = DO_LOGIN
    login = Login(method)

    @pytest.fixture(autouse=True)
    def setup(self):
        registration = Registration(DOREGISTER)
        self.user_data = registration.generator_user_data()
        registration.sent_registration_request(email=self.user_data['user_email'], password=self.user_data['password'],
                                               name=self.user_data['user_name'])

    def test_login_valid_credentials(self):
        response = self.login.sent_login_request(self.user_data['user_email'], self.user_data['password'])
        self.login.should_be_status_code_200(response)
        self.login.should_be_text_result_true(response)

    def test_login_invalid_password(self):
        wrong_passwrd = datetime.now().strftime("Hello%d%m%Y-%H-%M-%S-%f")
        response = self.login.sent_login_request(self.user_data['user_email'], wrong_passwrd)
        self.login.should_be_status_code_200(response)
        self.login.should_be_text_result_false(response)

    def test_login_invalid_email(self):
        wrong_user_email = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f") + '@test.test'
        response = self.login.sent_login_request(wrong_user_email, self.user_data['password'])
        self.login.should_be_status_code_200(response)
        self.login.should_be_text_result_false(response)
