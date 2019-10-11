import json

from .base_methods import BaseMethod
import requests
from ..set_urls import DO_LOGIN


class Login(BaseMethod):

    def sent_login_request(self, email, password):
        result = requests.post(self.api_path(DO_LOGIN), data={
            'email': email,
            'password': password
        })
        return result

    def should_be_text_result_true(self, response_data):
        response_result = json.loads(response_data.text)
        assert response_result['result'] is True, 'Result of response IS NOT "true"'

    def should_be_text_result_false(self, response_data):
        response_result = json.loads(response_data.text)
        assert response_result['result'] is False, 'Result of response IS NOT "false"'
