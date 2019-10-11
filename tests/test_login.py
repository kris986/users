import pytest
from ..set_urls import DO_LOGIN
from ..steps.login import Login


@pytest.mark.login
class TestLogin:
    method = DO_LOGIN
    login = Login(method)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.user_name = '11.08.2019-23-06-59@test.test'
        self.password = '1234567'

    def test_login_valid_data(self):
        result = self.login.sent_login_request(self.user_name, self.password)
        self.login.should_be_status_code_200(result)
        self.login.should_be_text_result_true(result)
