import pytest

from ..set_urls import DO_LOGIN
from ..steps.login import Login


@pytest.mark.login
class TestLogin:
    method = DO_LOGIN
    login = Login(method)

    @pytest.fixture(scope='function')
    def setup(self):
        self.user_name = ''
        self.password = ''

    def test_login_valid_data(self, setup):
        self.login.login_with_valid_credentials(self.user_name, self.password)
        self.login.should_be_status_code_200()
