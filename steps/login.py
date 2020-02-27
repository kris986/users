import json

from .base_methods import BaseMethod
from ..set_urls import DO_LOGIN


class Login(BaseMethod):

    def __init__(self, method=DO_LOGIN):
        self.method = method

    def should_be_text_result_true(self):
        response_result = json.loads(self.response.text)
        assert response_result['result'] is True, 'Result of response IS NOT "true"'

    def should_be_text_result_false(self):
        response_result = json.loads(self.response.text)
        assert response_result['result'] is False, 'Result of response IS NOT "false"'
