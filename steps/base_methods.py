from urllib.parse import urljoin

from users.set_urls import API_URL


class BaseMethod:
    def __init__(self, method):
        self.method = method

    def api_path(self, method):
        method_url = urljoin(API_URL, method)
        return method_url
