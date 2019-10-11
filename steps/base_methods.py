from urllib.parse import urljoin

from users.set_urls import API_URL


class BaseMethod:
    def __init__(self, method):
        self.method = method

    def api_path(self, method):
        method_url = urljoin(API_URL, method)
        return method_url

    def should_be_status_code_200(self, result):
        assert result.status_code == 200, 'Status code IS NOT 200 ok'

    def should_be_status_code_401(self, result):
        assert result.status_code == 401, 'Status code IS NOT 401'

    def should_be_status_code_403(self, result):
        assert result.status_code == 403, 'Status code IS NOT 403'
