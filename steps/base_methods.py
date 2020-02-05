from datetime import datetime
from urllib.parse import urljoin

from users.set_urls import API_URL


class BaseMethod:
    def __init__(self, method):
        self.method = method

    def api_path(self, method):
        method_url = urljoin(API_URL, method)
        return method_url

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
        assert result.status_code == 201, 'Status code IS NOT 200 ok'

    def should_be_status_code_401(self, result):
        assert result.status_code == 401, 'Status code IS NOT 401'

    def should_be_status_code_403(self, result):
        assert result.status_code == 403, 'Status code IS NOT 403'
