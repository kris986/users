import json

import allure

from .base_methods import BaseMethod
import requests


class Login(BaseMethod):
    response = None

    @allure.step
    def sent_login_request(self, email, password):
        self.response = requests.post(self.api_path(), data={
            'email': email,
            'password': password
        })
        return self.response

    def should_be_text_result_true(self):
        response_result = json.loads(self.response.text)
        assert response_result['result'] is True, 'Result of response IS NOT "true"'

    def should_be_text_result_false(self):
        response_result = json.loads(self.response.text)
        assert response_result['result'] is False, 'Result of response IS NOT "false"'
