import json

import allure
from datetime import datetime
from urllib.parse import urljoin

from users.set_urls import API_URL


class BaseMethod:
    def __init__(self, method):
        self.method = method

    def api_path(self):
        method_url = urljoin(API_URL, self.method)
        return method_url

    @allure.step
    def generator_user_data(self):
        gen_unique_part = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f")
        user_email = f'{gen_unique_part}@test.test'
        user_name = f'Name-{gen_unique_part}'
        password = f'PASS{gen_unique_part}'
        user_data = {'user_email': user_email,
                     'user_name': user_name,
                     'password': password}
        return user_data

    def should_be_status_code_200(self, result):
        assert result.status_code == 200, 'Status code IS NOT 200 ok'

    def should_be_status_code_401(self, result):
        assert result.status_code == 401, 'Status code IS NOT 401'

    def should_be_status_code_403(self, result):
        assert result.status_code == 403, 'Status code IS NOT 403'

    def should_be_error_msg_for_error_field(self, response, error_field):
        response_result = json.loads(response.text)
        assert 'type' in response_result, 'There is not requared type field'
        assert response_result['type'] == 'error', 'Error IS NOT arise, but it must'
        assert error_field in response_result['message'], 'There IS NOT details in the Error message'
